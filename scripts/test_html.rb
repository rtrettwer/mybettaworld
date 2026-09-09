#!/usr/bin/env ruby
# Jekyll HTML Proofer Test
# Testet die generierte Website auf tote Links, fehlende Bilder, etc.

require 'html-proofer'

options = {
  assume_extension: true,
  check_html: true,
  check_img_http: true,
  disable_external: true,  # Externe Links nicht prüfen (zu langsam)
  enforce_https: false,
  ignore_urls: [
    /localhost/,
    /127\.0\.0\.1/,
    /example\.com/
  ],
  ignore_files: [
    /_site\/assets\//,
    /_site\/vendor\//
  ],
  log_level: :info,
  only_4xx: true,
  typhoeus: {
    timeout: 30,
    connecttimeout: 30
  }
}

# Build Jekyll site first
script_dir = File.dirname(File.expand_path(__FILE__))
repo_root = File.dirname(script_dir) # scripts/ -> repo root
docs_dir = File.join(repo_root, 'docs')

puts "Building Jekyll site from: #{docs_dir}"
Dir.chdir(docs_dir) do
  system('bundle exec jekyll build') || exit(1)
end

puts "\nRunning HTML Proofer..."
HTMLProofer.check_directory(File.join(docs_dir, '_site'), options).run
