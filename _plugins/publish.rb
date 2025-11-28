require 'fileutils'
Jekyll::Hooks.register :site, :post_write do |site|
    # next if site.config['serving'] == true

    Dir.mkdir 'docs' unless File.directory? 'docs'
    FileUtils.cp_r(Dir.glob('_site/*'), 'docs')
end