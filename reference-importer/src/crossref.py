#!/usr/bin/python
# encoding: utf-8

import re
import sys
from workflow import Workflow

# get query from user
query = sys.argv[1]

def main(wf):
    from habanero import Crossref
    cr = Crossref()

    if re.match(r'^10.\d{4,9}.+$', query):
        
        r = cr.works(ids = query)
        item = r['message']
        uid = item['DOI']
        title = item['title'][0]
        journal = []
        if 'container-title' in item:
            journal = item['container-title'][0]
        elif 'short-container-title' in item:
            journal = item['short-container-title'][0]
        elif 'institution' in item:
            journal = item['institution']['name']
        subtitle = []
        if 'author' in item:
            for author in item['author']:
                auth = author['given'] + ", " + author['family']
                subtitle.append(auth)
            subtitle = '; '.join(subtitle)
        subtitle = subtitle + ' in Source: ' + journal

        wf.add_item(uid = uid,
            title = title,
            subtitle = subtitle,
            arg = uid,
            valid = True,
            icon = "crossref.png")
        wf.send_feedback()
    
    else:

        r = cr.works(query = query)
        items = r['message']['items']

        for item in items:
            uid = item['DOI']
            title = []
            if 'title' in item:
                title = item['title'][0]
            journal = []
            if 'container-title' in item:
                journal = item['container-title'][0]
            elif 'short-container-title' in item:
                journal = item['short-container-title'][0]
            elif 'institution' in item:
                journal = item['institution'][0]
            authors = []
            if 'author' in item:
                for author in item['author']:
                    if (('given' in author) and ('family' in author)):
                        auth = author['given'] + ", " + author['family']
                        authors.append(auth)
            subtitle = '; '.join(authors) + ' in Source: ' + ''.join(journal)

            wf.add_item(uid = uid,
                title = title,
                subtitle = subtitle,
                arg = uid,
                valid = True,
                icon = "crossref.png")
        wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
