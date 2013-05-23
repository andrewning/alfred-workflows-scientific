#!/usr/bin/env python
# encoding: utf-8
"""
bib.py

Created by Andrew Ning on April 4, 2013
"""

import requests
import sys
from subprocess import Popen, PIPE
from unicode_to_latex import unicode_to_latex
import re


# get the DOI
doi = sys.argv[1]

# use REST API (see http://crosscite.org/cn/)
headers = {'Accept': 'application/x-bibtex'}
r = requests.post('http://dx.doi.org/' + doi, headers=headers)

# convert to latex format
bibtex = r.text
for key in unicode_to_latex.keys():
    bibtex = bibtex.replace(key, unicode_to_latex[key])

# replace cite-key to allow bibtex to generate own
bibtex = re.sub('{.*?,', '{cite-key,', bibtex, count=1)


# occasionally the record doesn't exist
if bibtex[0] != '@':
    sys.stdout.write('BibTeX Not Available')
    exit()

# open BibDesk (opens a document if you have this set in BibTeX preferences)
p = Popen(['open', '-a', 'BibDesk'], stderr=PIPE, stdout=PIPE)
p.communicate()


# applescript to import into BibDesk
script = '''
if exists application "BibDesk" then
    tell application "BibDesk"
        activate
        if (count of documents) > 0 then
            tell document 1
                import from "{0}"
            end tell
        end if
    end tell
end if
'''.format(bibtex.replace('\\', '\\\\').replace('"', '\\"'))

# run applescript
p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE)  # , stderr=PIPE)
p.communicate(script)

# pass bibtex
sys.stdout.write(bibtex)

