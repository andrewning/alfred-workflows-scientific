#!/usr/bin/env python
# encoding: utf-8
"""
bib_gscholar.py

Created by Andrew Ning on November 16, 2013
"""

import sys
import requests
import hashlib
import random

from common import importBibTeXIntoBibDesk


# get the links
data = sys.argv[1].split('***')  # custom delimiter
bibtex_link = data[0]
pdf_link = data[1]

if pdf_link == 'None':
    pdf_link = None


# set headers (thank you: http://blog.venthur.de/index.php/2010/01/query-google-scholar-using-python/)
google_id = hashlib.md5(str(random.random())).hexdigest()[:16]
headers = {'User-Agent': 'Mozilla/5.0',
           'Cookie': 'GSP=ID=%s:CF=4' % google_id}

# grab bibtex
r = requests.get(bibtex_link, headers=headers)
bibtex = r.text

importBibTeXIntoBibDesk(bibtex, pdf_link)
