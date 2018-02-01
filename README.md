to build

	sh build.sh

output will be written to

	tikz-images/*.pdf => example.tex => example.pdf
	tikz-images/*.png => example.html

To process pandoc, it uses a filter. This python thing uses stdin/out to process JSON.

In order to output some debug info, we log to `log.txt` from `tikz.py`

#### references

- http://pandoc.org/filters.html
- https://github.com/jgm/pandocfilters

