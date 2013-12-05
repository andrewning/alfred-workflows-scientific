#!/usr/bin/env python
# encoding: utf-8
"""
common.py

Created by Andrew Ning on 2013-11-17.
"""

import sys
from subprocess import Popen, PIPE
from unicode_to_latex import unicode_to_latex
import re
import requests
import os
import time
import alfred



months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def waitForPeriodInQuery(title, icon=None):
    """waits for user to end query with '.' before actually initiating search"""

    # get query from user
    query = sys.argv[1]

    if icon is None:
        icon = 'icon.png'

    if query[-1] != '.':

        results = [alfred.Item(title=title,
                           subtitle="end query with . to execute search",
                           attributes={'uid': 'none'},
                           icon=icon)]

        sys.stdout.write(alfred.xml(results))
        exit()

    return query[:-1]



def cachePDFLocation(pdfpath):
    """cache the location of the pdf for later use"""

    f = open('pdflocation', 'w')
    f.write(pdfpath + '\n')
    f.write(str(time.time()))
    f.close()


def retreivePDFLocation():
    """get the cached PDF location and clear the file"""

    try:
        # see if a path was cached
        f = open('pdflocation', 'r')
        pdfpath = f.readline().rstrip()  # remove trailing newline
        timestamp = float(f.readline())
        f.close()

        # now remove the file so its not used again later
        os.remove('pdflocation')

        # check if this was cached recently
        if time.time() - timestamp > 60.0:  # if it's been more than a minute then cache is probably unintentional
            pdfpath = None

    except IOError:
        # no cached file
        pdfpath = None

    return pdfpath


def runAppleScript(script):

    Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE).communicate(script)



def runAlfredSearch(search, query):
    '''run Alfred script filter for Citation Search'''

    script = '''
    tell application "Alfred 2" to search "{0} {1}"
    '''.format(search, query.replace('\\', '\\\\').replace('"', '\\"'))
    runAppleScript(script)




def importBibTeXIntoBibDesk(bibtex, withPDFURL=None):

    # check if valid BibTeX
    if bibtex[0] != '@':
        sys.stdout.write('BibTeX Not Available')
        exit()

    # convert to latex format (e.g., & -> \&)
    for key in unicode_to_latex.keys():
        bibtex = bibtex.replace(key, unicode_to_latex[key])

    # replace cite-key to allow bibtex to generate own
    bibtex = re.sub('{.*?,', '{cite-key,', bibtex, count=1)

    # open BibDesk (opens a document if you have this set in BibTeX preferences)
    p = Popen(['open', '-a', 'BibDesk'], stderr=PIPE, stdout=PIPE)
    p.communicate()

    # check if file cached first
    filename = retreivePDFLocation()

    # Download PDF is necessary and possible
    if filename is None and withPDFURL is not None:

        r = requests.get(withPDFURL, stream=True)
        filename = os.path.join(os.path.expanduser('~'), 'Downloads', 'temp.pdf')

        # remove any existing copies of this file
        try:
            os.remove(filename)
        except OSError:
            pass

        # check if the URL is actually for a PDF
        if r.headers['content-type'] == 'application/pdf':

            f = open(filename, 'wb')

            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

            f.close()



    # applescript to import into BibDesk
    script = '''
    tell application "Finder"
        set theFile to "{0}"
        if exists theFile as POSIX file then
            set fileExists to true
        else
            set fileExists to false
        end if
    end tell

    if exists application "BibDesk" then
        tell application "BibDesk"
            activate
            if (count of documents) > 0 then
                tell document 1
                    import from "{1}"
                    set thePubs to result
                    if (fileExists) and not (thePubs is missing value) and (count of thePubs) is 1 then
                        set thePub to item 1 of thePubs
                        tell thePub
                            make new linked file with data theFile at beginning of linked files
                            auto file
                        end tell
                    end if
                end tell
            end if
        end tell
    end if
    '''.format(filename, bibtex.replace('\\', '\\\\').replace('"', '\\"'))
    # set the clipboard to "{0}"

    runAppleScript(script)

    # pass bibtex through workflow
    sys.stdout.write(bibtex)



