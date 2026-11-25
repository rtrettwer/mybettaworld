#!/usr/bin/env ruby
require 'jekyll'

root = File.expand_path('../docs', __dir__)
site = Jekyll::Site.new(Jekyll.configuration('source' => root, 'quiet' => true))
site.read
site.tags.keys.sort.each do |tag|
  slug = Jekyll::Utils.slugify(tag)
  raise "Tag ohne gültigen URL-Slug: #{tag.inspect}" if slug.empty?

  path = File.join(root, 'tags', "#{slug}.md")
  yaml_tag = tag.to_yaml.delete_prefix('--- ').strip
  content = "---\nlayout: tag_home_blog\ntag: #{yaml_tag}\npermalink: /tags/#{slug}/\n---\n"
  next if File.exist?(path) && File.read(path) == content

  File.write(path, content)
  puts "Tag-Seite aktualisiert: #{slug}"
end

links_file = File.expand_path('keywords.yml', __dir__)
links = YAML.safe_load_file(links_file)
posts_by_slug = site.posts.docs.to_h do |post|
  [File.basename(post.path, '.md').sub(/\A\d{4}-\d{2}-\d{2}-/, ''), post]
end
updated_links = links.map do |entry|
  slug = entry.fetch('url').split('/').last.delete_suffix('.html')
  post = posts_by_slug.fetch(slug) { raise "Kein Post für Verlinkung: #{entry.fetch('key')}" }
  entry.merge('url' => post.url.delete_suffix('.html'))
end
if links != updated_links
  File.write(links_file, updated_links.to_yaml)
  puts 'Post-Links an die tatsächlichen Jekyll-URLs angepasst.'
end
