require 'fileutils'
require 'open3'
require 'tmpdir'

checker = File.expand_path('../scripts/test_html.rb', __dir__)
Dir.mktmpdir('website-html-') do |site|
  check = lambda do |expected_success|
    output, status = Open3.capture2e('ruby', checker, site)
    raise output unless status.success? == expected_success
  end
  check.call(false)
  File.write(File.join(site, 'index.html'), '<a href="/post#detail">Post</a>')
  File.write(File.join(site, 'post.html'), '<h1 id="detail">Post</h1>')
  check.call(true)
  File.write(File.join(site, 'index.html'), '<a href="/post#missing">Fehlender Anker</a>')
  check.call(false)
  File.write(File.join(site, 'index.html'), '<img src="/missing.webp" alt="Fehlendes Bild">')
  check.call(false)
  File.write(File.join(site, 'index.html'), '<a href="https://trettwer.de/missing">Fehlender interner Link</a>')
  check.call(false)
end
puts 'HTML-Prüfung erkennt fehlende Builds, Bilder, Links und Anker.'
