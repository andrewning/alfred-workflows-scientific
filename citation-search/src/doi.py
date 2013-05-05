#!/usr/bin/env python
# encoding: utf-8
"""
doi.py

Created by Andrew Ning on April 4, 2013
"""


import requests
import alfred
import sys

# get query from user
query = sys.argv[1]

if query.endswith('!!'):
    doi = query.split('!!')[0].rstrip().lstrip()
    results = [alfred.Item(title='Lookup by DOI: ' + doi,
                           subtitle='Import BibTeX',
                           attributes={'uid': doi, 'arg': doi},
                           icon='icon.png')]

else:

    # Use crossref metadata search (beta) to get the DOI
    params = {'q': query, 'rows': '10'}
    r = requests.get('http://search.labs.crossref.org/dois', params=params)

    # write results in XML format for Alfred
    results = []
    for j in r.json():
        results.append(alfred.Item(title=j['fullCitation'],
                                   subtitle='Import BibTeX',
                                   attributes={'uid': j['doi'], 'arg': j['doi']},
                                   icon='icon.png'))

sys.stdout.write(alfred.xml(results))



