#!/usr/bin/env python
# encoding: utf-8
"""
bib_gscholar.py

Created by Andrew Ning on November 16, 2013
"""

import sys
from subprocess import Popen, PIPE


# get the DOI
bibtex = sys.argv[1]

print bibtex

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

