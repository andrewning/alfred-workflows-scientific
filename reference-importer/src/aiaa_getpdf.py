#!/usr/bin/env python
# encoding: utf-8
"""
openurl.py

Created by Andrew Ning on 4/29/2013
"""

import sys
from subprocess import call

# get query from user
query = sys.argv[1]
doi = query.split('***')[0]

# assemble url and open in default browser
url = 'http://arc.aiaa.org/doi/pdf/' + doi
call(['open', url])
