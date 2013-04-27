#!/usr/bin/env python
# encoding: utf-8
"""
scrape.py

Created by Andrew Ning on April 8, 2013
"""

import cPickle as pickle

from bs4 import BeautifulSoup
import requests

# initialize dictionary
results = {}

# scrape numpy index
r = requests.get('http://docs.scipy.org/doc/numpy/genindex.html')
soup = BeautifulSoup(r.text)
all_methods = soup.find_all('dt')

# iterate through methods
for method in all_methods:
    anchor = method.a

    if anchor:  # check if link exists

        text = anchor.contents[0]  # description of link
        if '(in module numpy)' in text:

            # save only name *(without parens)
            name = text.split(' (in module numpy)')[0].split('(')[0]

            # save link and follow it to get description
            link = 'http://docs.scipy.org/doc/numpy/' + anchor.get('href')
            r = requests.get(link)
            soup2 = BeautifulSoup(r.text)
            middle = soup2.find('dd')
            if middle:
                description = middle.p.contents[0]
            else:
                description = ''

            # encode
            name = name.encode('utf-8')
            link = link.encode('utf-8')
            description = description.encode('utf-8')

            # add to dictionary
            results[name] = (description, link)
            print name

# save to file
pickle.dump(results, open('data.pickle', 'wb'))

