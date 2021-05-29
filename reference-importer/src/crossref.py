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
        journal = item['short-container-title'][0]
        arg = item['DOI']
        subtitle = []
        if 'author' in item:
            for author in item['author']:
                auth = author['given'] + ", " + author['family']
                subtitle.append(auth)
            subtitle = '; '.join(subtitle)
        subtitle = subtitle + ' in Journal: ' + journal

        wf.add_item(uid = uid,
            title = title,
            subtitle = subtitle,
            arg = arg,
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
            if 'short-container-title' in item:
                journal = item['short-container-title'][0]
            arg = item['DOI']
            subtitle = []
            if 'author' in item:
                for author in item['author']:
                    if (('given' in author) and ('family' in author)):
                        auth = author['given'] + ", " + author['family']
                        subtitle.append(auth)
                subtitle = '; '.join(subtitle)
            subtitle = ''.join([str(elem) for elem in subtitle]) + ' in Journal: ' + ''.join([str(elem) for elem in journal])

            wf.add_item(uid = uid,
                title = title,
                subtitle = subtitle,
                arg = arg,
                valid = True,
                icon = "crossref.png")
        wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))