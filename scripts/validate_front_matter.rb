#!/usr/bin/env ruby
# Front-Matter-Validierung fuer Fisch- und Aquarien-Posts
# Prueft Pflichtfelder und Konsistenz (z.B. fish_death_date ohne fish_status),
# damit Daten-Bugs wie ein faelschlich als "aktiv" angezeigter toter Fisch
# schon vor dem Deploy auffallen.

require 'yaml'
require 'date'

POSTS_DIR = File.join(__dir__, '..', 'docs', '_posts')
errors = []

def front_matter(path)
  content = File.read(path)
  return nil unless content.start_with?('---')

  _, fm, = content.split(/^---\s*$/, 3)
  YAML.safe_load(fm, permitted_classes: [Date, Time], aliases: true) || {}
end

Dir.glob(File.join(POSTS_DIR, '*.md')).sort.each do |path|
  file = File.basename(path)
  data = front_matter(path)
  next if data.nil?

  categories = Array(data['categories'])

  if categories.include?('fish')
    errors << "#{file}: 'title' fehlt" if data['title'].to_s.strip.empty?
    errors << "#{file}: 'fish_arrival' fehlt" if data['fish_arrival'].to_s.strip.empty?

    status = data['fish_status'].to_s.strip
    death_date = data['fish_death_date'].to_s.strip
    sold_date = data['fish_sold_date'].to_s.strip

    unless status.empty? || %w[active deceased sold].include?(status)
      errors << "#{file}: unbekannter fish_status '#{status}' (erlaubt: active, deceased, sold)"
    end

    if status == 'deceased' && death_date.empty?
      errors << "#{file}: fish_status ist 'deceased', aber 'fish_death_date' fehlt"
    end
    if status == 'sold' && sold_date.empty?
      errors << "#{file}: fish_status ist 'sold', aber 'fish_sold_date' fehlt"
    end
    if !death_date.empty? && status != 'deceased'
      errors << "#{file}: 'fish_death_date' gesetzt, aber fish_status ist nicht 'deceased' (aktuell: '#{status}') - Fisch wird faelschlich als aktiv angezeigt!"
    end
    if !sold_date.empty? && status != 'sold'
      errors << "#{file}: 'fish_sold_date' gesetzt, aber fish_status ist nicht 'sold' (aktuell: '#{status}') - Fisch wird faelschlich als aktiv angezeigt!"
    end
  end

  next unless categories.include?('tank')

  errors << "#{file}: 'title' fehlt" if data['title'].to_s.strip.empty?
  if data['aktiv'].nil?
    errors << "#{file}: 'aktiv' (true/false) fehlt"
  elsif data['aktiv'] == false && data['inaktiv_seit'].to_s.strip.empty?
    errors << "#{file}: aktiv ist false, aber 'inaktiv_seit' fehlt"
  end
end

if errors.empty?
  puts "✅ Front Matter aller Fisch- und Aquarien-Posts ist konsistent."
  exit 0
else
  puts "❌ Front-Matter-Probleme gefunden:\n\n"
  errors.each { |e| puts "  - #{e}" }
  puts "\n#{errors.size} Problem(e) gefunden."
  exit 1
end
