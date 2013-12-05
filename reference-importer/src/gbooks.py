#!/usr/bin/env python
# encoding: utf-8
"""
gbooks.py

Created by Andrew Ning on November 16, 2013
"""


import requests
import alfred
import sys

from common import months  # , waitForEndOfQuery


# get query from user
# query = waitForEndOfQuery('Search Using Book Metadata', 'gbooks.jpg')
query = sys.argv[1]

params = {'q': query, 'maxResults': 10, 'fields': 'items(volumeInfo(title,subtitle,authors,publisher,publishedDate,industryIdentifiers))'}

# search on google books
r = requests.get('https://www.googleapis.com/books/v1/volumes', params=params)

results = []

for item in r.json()['items']:
    info = item['volumeInfo']

    title = ''
    authors = ''
    publisher = ''
    publishedDate = ''
    year = ''
    month = ''
    isbn = ''
    infoString = ''

    if 'title' in info:
        title = info['title']

    if 'subtitle' in info:
        title += ": " + info['subtitle']

    if 'authors' in info:
        authors = ' and '.join(info['authors'])
        infoString = ', '.join(info['authors'])

    if 'publishedDate' in info:
        publishedDate = info['publishedDate']
        entries = publishedDate.split('-')
        year = entries[0]
        infoString += ', ' + year
        if len(entries) > 1:
            month = months[int(entries[1]) - 1]

    if 'publisher' in info:
        publisher = info['publisher']
        infoString += ', ' + publisher

    if 'industryIdentifiers' in info:
        for idnt in info['industryIdentifiers']:
            if idnt['type'] == 'ISBN_10':
                isbn = idnt['identifier']

    bibtex = u"""@book{{{},
    Title = {{{}}},
    Publisher = {{{}}},
    Year = {{{}}},
    Author = {{{}}},
    Month = {{{}}},
    ISBN = {{{}}}
    }}
    """.format('cite-key', title, publisher, year, authors, month, isbn)


    results.append(alfred.Item(title=title,
                               subtitle=infoString,
                               attributes={'uid': isbn, 'arg': bibtex},
                               icon='gbooks.jpg'))

alfred.write(alfred.xml(results))





