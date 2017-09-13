ggl
===
Google right from your command line
-----------------------------------

Do you ever need to perform a quick google search while on command line?
Well that's exactly what ggl is for, it lets you open your browser on your query without the hassle. You can also search:
- Google Images
- YouTube
- Stackoverflow
- Wikipedia
- DuckDuckGo
- Github

See usage for more info.

Installation
------------
```sh
gem install ggl
```

If you're not on OSX you need to have ```xdg-open``` installed.

Usage
-----
```sh
ggl [query]                                 simple google search
ggl -i/--images [query]                     google images search
ggl -y/--youtube [query]                    youtube search
ggl -s/--stack/--stackoverflow [query]      search stackoverflow (oh yes)
ggl -w/--wiki/--wikipedia [query]           search wikipedia
ggl -d/--ddg/--duckduckgo [query]           search duckduckgo
ggl -g/--git/--github [query]               search github

```
License
-------

MIT © [Justyna Rachowicz](https://github.com/mrowa44)
