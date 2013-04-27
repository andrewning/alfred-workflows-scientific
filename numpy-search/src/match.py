#!/usr/bin/env python
# encoding: utf-8
"""
match.py

Created by Andrew Ning on April 8, 2013
"""

import sys
import cPickle as pickle
from difflib import get_close_matches
import alfred

# get query from user
query = sys.argv[1]

# load numpy methods
methods = pickle.load(open('data.pickle', 'rb'))

# check for matches
matches = get_close_matches(query, methods.keys(), n=10, cutoff=0.5)

# write results in XML format for Alfred
results = []
for match in matches:
    results.append(alfred.Item(title=match,
                               subtitle=methods[match][0],
                               attributes={'uid': match, 'arg': methods[match][1]},
                               icon='scipy.png'))

sys.stdout.write(alfred.xml(results))



