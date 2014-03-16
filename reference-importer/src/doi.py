#!/usr/bin/env python
# encoding: utf-8
"""
doi2bib.py

Created by Andrew Ning on April 4, 2013
"""

import requests
import sys
import re
from subprocess import call

from common import importBibTeXIntoBibDesk, runAppleScript


# get the DOI
doi = sys.argv[1]
action = sys.argv[2]

if action == 'bibtex':

    # use REST API (see http://crosscite.org/cn/)
    headers = {'Accept': 'application/x-bibtex'}
    r = requests.post('http://dx.doi.org/' + doi, headers=headers)

    # extract bibtex
    r.encoding = 'utf-8'
    bibtex = r.text
    bibtex = bibtex.replace('&amp;', '&')
    bibtex = bibtex.strip()

    # figure out which Journal (if any) this is
    PDFURL = None
    match = re.search('[jJ]ournal\s*=\s*\{(.*?)\}', bibtex)
    Journal = ''
    if match:
        Journal = match.group(1)

    # get PDF for Wind Energy
    if Journal == 'Wind Energy':
        PDFURL = 'http://onlinelibrary.wiley.com/doi/' + doi + '/pdf'

    # [INSERT HERE: if you want to try to auto link a PDF from some other journal
    #   follow the example above for Wind Energy.  I've already parsed out the
    #   journal name.  You could potentially parse out other bits of info from the
    #   BibTeX as search criteria. ]

    # import bibtex
    importBibTeXIntoBibDesk(bibtex, PDFURL)



elif action == 'url':

    call(['open', 'http://dx.doi.org/' + doi])


elif action == 'ref':

    style = 'apa'  # hard-coded for now
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


    script = '''
    set the clipboard to "{0}"
    '''.format(ref.replace('\\', '\\\\').replace('"', '\\"'))
    runAppleScript(script)

    sys.stdout.write(ref)





