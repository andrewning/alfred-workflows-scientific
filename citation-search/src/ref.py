#!/usr/bin/env python
# encoding: utf-8
"""
ref.py

Created by Andrew Ning on 2013-05-01.
"""

import requests
import sys


# get the DOI
doi = sys.argv[1]

style = 'apa'
locale = 'en-US'

# use REST API (see http://crosscite.org/cn/)
reftype = 'text/x-bibliography; style={0}; locale={1}'.format(style, locale)

headers = {'Accept': reftype}
r = requests.post('http://dx.doi.org/' + doi, headers=headers,
                  allow_redirects=True)

# get encoding type
contentType = r.headers['content-type']
if contentType and 'charset=' in contentType:
    charset = contentType.split('charset=')[1].lstrip().rstrip()
else:
    charset = 'utf-8'

ref = r.text.encode(charset)

# check if style works
if int(r.headers['content-length']) == 0:
    sys.stdout.write('Style not available')
    exit()

# check if DOI exists
if 'DOI Not Found' in ref:
    sys.stdout.write('DOI Not Found')
    exit()

sys.stdout.write(ref)

