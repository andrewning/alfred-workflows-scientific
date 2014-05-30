#!/usr/bin/env python
# encoding: utf-8
"""
pdf2doi.py

Created by Andrew Ning on 2013-11-16.
"""

import re
import subprocess
import sys

from common import cachePDFLocation, runAlfredSearch


# get query from user
pdffile = sys.argv[1]

# extract text of first page
txt = subprocess.Popen(["./pdftotext", "-q", "-l", "1", pdffile, "-"], stdout=subprocess.PIPE).communicate()[0]


# try to get DOI
result = re.search('[Dd][Oo][Ii][\s\.\:]{0,2}(.*?)[\s\n\]\)\}]+', txt)
if result is None:
    result = re.search('\\b(10[.][0-9]{4,}(?:[.][0-89]+)*/(?:(?!["&\'])\S)+)\\b', txt)

if result is not None:
    doi = result.group(1)

    # check if this was actually a URL
    if doi.startswith('org/'):
        doi = doi[4:]

else:
    # couldn't find DOI, grab the first dozen capitalized words as a fallback
    words = re.sub("\W", " ", txt).strip().split()

    phrase = []
    total = 12
    for word in words:
        if len(phrase) >= total:
            break
        if word[0].isupper():
            phrase.append(word)

    doi = ' '.join(phrase)


# Check for AIAA to use specialized search
result = re.search('AIAA', txt)
if result is None:
    result = re.search('American Institute of Aeronautics and Astronautics', txt)

if result is not None:
    search = 'aiaa'
else:
    search = 'ref'


# copy file to temporary location
cachePDFLocation(pdffile)

# run script filter for Citation Search
runAlfredSearch(search, doi)


