#!/usr/bin/env python
# encoding: utf-8
"""
gscholar.py

Created by Andrew Ning on November 16, 2013
"""


import requests
import alfred
from bs4 import BeautifulSoup  # , SoupStrainer
import hashlib
import random

from common import waitForPeriodInQuery


# get query from user (won't parse until ends with ".")
title='Google Scholar Search'
icon = 'gscholar.png'
query = waitForPeriodInQuery(title, icon)


params = {'q': query}

# set headers (thank you: http://blog.venthur.de/index.php/2010/01/query-google-scholar-using-python/)
google_id = hashlib.md5(str(random.random())).hexdigest()[:16]
headers = {'User-Agent': 'Mozilla/5.0',
           'Cookie': 'GSP=ID=%s:CF=4' % google_id}


# search on google cscholar
r = requests.get('http://scholar.google.com/scholar', params=params, headers=headers)
# r.encoding = 'utf-8'

# parse data
# only_articles = SoupStrainer('div', {'class': 'gs_r'})
# articles = BeautifulSoup(r.text, 'html.parser', parse_only=only_articles)
soup = BeautifulSoup(r.text, 'html5lib')

# get all articles
articles = soup.find_all('div', {'class': 'gs_r'})

results = []
for art in articles:

    data = art.find('div', {'class': 'gs_ri'})

    if data is None:
        continue  # skip this one

    # get title
    # title = art.find('h3', {'class': 'gs_rt'}).a.contents[0]
    title = data.find('h3', {'class': 'gs_rt'})
    title = ''.join(title.findAll(text=True))
    if title[0] == '[':
        entries = title.split(']')
        title = entries[0] + ']' + entries[2]

    # author data
    author_fields = data.find('div', {'class': 'gs_a'})
    author_data = ''.join(author_fields.findAll(text=True))  # .encode('utf-8')

    # bibtex link
    links = data.find('div', {'class': 'gs_fl'})
    bibtex_link = links.find('a', href=True, text='Import into BibTeX')['href']
    bibtex_link = 'http://scholar.google.com' + bibtex_link

    # pdf link
    sidedata = art.find('div', {'class': 'gs_ggs'})
    pdflink = 'None'
    if sidedata:
        pdfdata = sidedata.find('div', {'class': 'gs_md_wp'})
        pdflink = pdfdata.a['href']


    # a unique id
    some_id = bibtex_link.split(':')[2]

    # concatenate arguments with delimter
    delimter = '***'  # a custom delimeter
    arg = bibtex_link + delimter + pdflink

    results.append(alfred.Item(title=title,
                               subtitle=author_data,
                               attributes={'uid': some_id, 'arg': arg},
                               icon='gscholar.png'))

alfred.write(alfred.xml(results))


