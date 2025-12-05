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
puts "Building Jekyll site..."
system('cd docs && bundle exec jekyll build') || exit(1)

puts "\nRunning HTML Proofer..."
HTMLProofer.check_directory('./docs/_site', options).run
