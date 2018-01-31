#! /bin/bash

pandoc --filter ./tikz.py -t html -f markdown example.md -s -o example.html
pandoc --filter ./tikz.py -t latex -f markdown example.md -s -o example.tex
pdflatex example.tex
