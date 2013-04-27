alfred-workflows-scientific
===========================

A collection of [Alfred v2](http://www.alfredapp.com) workflows (mostly) targeting scientific applications.  Use of workflows requires the Alfred PowerPack.

- [NumPy Search](#numpy-search): search methods within the NumPy module and open the associated documentation in your browser.
- [BibTeX Grab](#bibtex-grab): lookup articles using any metadata and download the associated BibTeX entry (article's DOI must registered with IDF).
- [AIAA Search](#aiaa-search): lookup AIAA articles using any metadata and download the associated BibTeX entry or the actual PDF (AIAA subscription required for PDF).



NumPy Search
------------

![](screenshots/np.tiff)

**np "method name"**

Search the methods in the NumPy module, and see a short description from the docstring. Actioning the item opens the documentation for the method in your browser.  Useful if you can't quite remember the name of one of the methods (e.g, atan or arctan), or if can't remember the order of the arguments for one of the methods and want to pull it up in your browser.  Currently, NumPy Search only includes methods that are directly in the numpy module and not in submodules (e.g., numpy.polynomial or numpy.linalg)

**scrapenp**

The workflow contains a cached version of the relevant information from the NumPy docs.  If NumPy is updated and the local cache is out of date, you can run "scrapenp" to redownload the relevant data.  Be patient though, as it will take a few minutes.  A notification will pop-up when its complete.

#### [[Download NumPy Search](https://github.com/andrewning/alfred-workflows-scientific/raw/master/numpy-search/NumPy%20Search.alfredworkflow)]



BibTeX Grab
-----------

![](screenshots/bib.tiff)

**bib "citation info"**

Uses a metadata search api (beta) provided by [CrossRef](http://search.labs.crossref.org).  You can search using any part of a citation (e.g., author names, article title, digital object identifier (DOI), etc.), or even a full citation.  It then grabs the BibTeX from the [International DOI Foundation](http://dx.doi.org) (IDF).  If a [BibDesk](http://bibdesk.sourceforge.net) document is open (or if you've set the preference in BibDesk to open a file at application launch), the BibTex entry will be directly imported.  For those that don't use BibDesk, the BibTeX reference is also copied to the clipboard.  Obviously the article you're interested in needs to have a registered DOI with IDF (generally only journal articles).  Occasionaly some articles don't have associated BibTeX data stored with them, and a "Not Available" notification will be posted.

#### [[Download BibTeX Grab](https://github.com/andrewning/alfred-workflows-scientific/raw/master/bibtex-grab/BibTeX%20Grab.alfredworkflow)]



AIAA Search
-----------

![](screenshots/aiaa.tiff)

**aiaa "citation info"**

Similar to BibTeX Grab, but specifically designed for searching for papers published with [The American Institute of Aeronautics and Astronautics](http://arc.aiaa.org) (AIAA).  If you're looking for an AIAA paper, this workflow is definitely preferrable to BibTeX Grab, as it contains all published AIAA papers (conference or journal).  There is no official API for this, so performance is a bit slower.  If a [BibDesk](http://bibdesk.sourceforge.net) document is open (or if you've set the preference in BibDesk to open a file at application launch), the BibTex entry will be directly imported.  For those that don't use BibDesk, the BibTeX reference is also copied to the clipboard.

**aiaa "citation info" [cmd]**

If you hold down [cmd] when actioning an article, the PDF will be downloaded directly from AIAA (an AIAA subscription is required).

#### [[Download AIAA Search](https://github.com/andrewning/alfred-workflows-scientific/raw/master/aiaa-search/AIAA%20Search.alfredworkflow)]


Acknowledgments
---------------

The following packages/modules are used within these workflows:

- [Requests](http://docs.python-requests.org/en/latest/), an HTTP library written in Python.
- [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/), a Python library for parsing HTML
- [alfred-python](https://github.com/nikipore/alfred-python), a lightweight wrapper to Alfred's workflow API

License
-------

Copyright (c) 2013, S. Andrew Ning.  All rights reserved.

All code is licensed under [The MIT License](http://opensource.org/licenses/mit-license.php).
