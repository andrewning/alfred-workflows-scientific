#!/bin/bash

path1=$(echo $1 | sed 's: /:,/:' | cut -d',' -f1)
path2=$(echo $1 | sed 's: /:,/:' | cut -d',' -f2)
base1=$(dirname "$path1")
base2=$(dirname "$path1")
rm -rf tmp
rm -f diff.pdf
cp -R "$base1" tmp
cp -R "$base2"/* tmp
cp "$path1" tmp/old.tex
cp "$path2" tmp/new.tex
cd tmp
../latexdiff old.tex new.tex > diff.tex
PATH=$PATH:/usr/texbin
latexmk -f -pdf diff.tex
cp diff.pdf ../
cd ../
rm -rf tmp
open diff.pdf


