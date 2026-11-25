#!/usr/bin/env ruby
require 'html-proofer'

site_dir = ARGV.fetch(0, File.expand_path('../docs/_site', __dir__))
abort 'Kein Build vorhanden. Bitte zuerst npm run build ausführen.' unless File.file?(File.join(site_dir, 'index.html'))

# GitHub Pages löst auch extensionlose Post-Links auf die jeweilige HTML-Datei auf.
HTMLProofer.check_directory(
  site_dir,
  assume_extension: '.html',
  disable_external: true,
  enforce_https: false,
  swap_urls: { %r{\Ahttps://trettwer\.de(?=/|\z)} => '' },
  log_level: :info
).run
