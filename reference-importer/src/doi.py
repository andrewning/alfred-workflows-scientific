#!/usr/bin/python
# encoding: utf-8

import sys
from workflow import Workflow
from subprocess import call
from habanero import cn

def main(wf):
    
    from habanero import cn
    from common import importBibTeXIntoBibDesk, runAppleScript

    # get the DOI
    doi = sys.argv[1]
    action = sys.argv[2]

    # fix escaped chars
    doi = doi.replace('\\', '')

    if action == 'bibtex':

        bibtex = cn.content_negotiation(ids = doi, format = "bibentry")

        PDFURL = None

        importBibTeXIntoBibDesk(bibtex, PDFURL)
    
    elif action == 'url':
        
        call(['open', 'http://dx.doi.org/' + doi])
    
    elif action == 'ref':

        ref = cn.content_negotiation(ids= doi, format="text", style="apa")

        script = '''
        set the clipboard to "{0}"
        '''.format(ref.replace('\\', '\\\\').replace('"', '\\"'))
        
        runAppleScript(script)

    sys.stdout.write(ref)


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
