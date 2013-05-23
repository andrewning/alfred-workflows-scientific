#!/usr/bin/env python
# encoding: utf-8
"""
bib.py

Created by Andrew Ning on April 15, 2013
"""

import requests
import sys
from subprocess import Popen, PIPE

# get doi
data = sys.argv[1].split('***')  # custom delimiter
doi = data[0]
authors = data[1]  # take author from html b.c. I've noticed author order
                   # is not always reliable in the citation
authors = authors.replace(',', ' and')


# get citation data
data = {'doi': doi,
        'include': 'cit'}
r = requests.get('http://arc.aiaa.org/action/downloadCitation', params=data)

# initialize
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# author = ''

# parse cit data
for line in r.text.split('\n'):
    key = line[0:2]
    value = line[2:].lstrip()[2:].rstrip()

    # if key == 'AU':
    #     if author == '':
    #         author = value
    #         firstAuthor = author
    #     else:
    #         author += ' and ' + value
    if key == 'TI':
        title = value
    elif key == 'T1':
        title = value
    elif key == 'PY':
        year = value
    elif key == 'T2':
        journal = value
    elif key == 'TY':
        pubtype = value
    elif key == 'VL':
        volume = value
    elif key == 'IS':
        number = value
    elif key == 'SP':
        startPage = value
    elif key == 'EP':
        endPage = value
        pages = startPage + '-' + endPage
    elif key == 'Y1':
        month = months[int(value.split('/')[1])]

firstAuthor = authors.split(' and')[0]
lastName = firstAuthor.split(' ')[-1]
# cite_key = lastName + year
cite_key = 'cite-key'


# if ',' in firstAuthor:
#     cite_key = firstAuthor.split(',')[0] + year
# else:
#     cite_key = firstAuthor.split(' ')[-1] + year



# convert to BibTeX format manually b.c. doesn't map well and AIAA adds some unncecessary data
if pubtype == 'CHAP':

    bibtex = """@inproceedings{{{},
    Author = {{{}}},
    Title = {{{}}},
    Booktitle = {{{}}},
    Month = {{{}}},
    Year = {{{}}},
    Doi = {{{}}}}}
    """.format(cite_key, authors, title, journal, month, year, doi)

elif pubtype == 'JOUR':

    bibtex = """@article{{{},
    Author = {{{}}},
    Title = {{{}}},
    Journal = {{{}}},
    Month = {{{}}},
    Year = {{{}}},
    Volume = {{{}}},
    Number = {{{}}},
    Pages = {{{}}},
    Doi = {{{}}}}}
    """.format(cite_key, authors, title, journal, month, year, volume, number, pages, doi)


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
'''.format(bibtex.replace('"', '\\"'))  # escape quotes

# run applescript
p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE)
p.communicate(script)

# pass bibtex
sys.stdout.write(bibtex)




