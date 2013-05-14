alfred-workflows-scientific
===========================

A collection of [Alfred v2](http://www.alfredapp.com) workflows targeting scientific applications.  Use of workflows requires the Alfred PowerPack.

- [NumPy Search](#numpy-search): search methods within the NumPy module and open the associated documentation in your browser.
- [Citation Search](#citation-search): lookup articles using any citation metadata and either download the associated BibTeX entry, go to the landing page for the article, or copy a formatted reference.
- [AIAA Search](#aiaa-search): lookup AIAA articles using any metadata and download the associated BibTeX entry or the actual PDF (AIAA subscription required for PDF).
- [LaTeX Tools](#latex-tools): tools for working with LaTeX files.  Currently a word/figure/equation count, and a diff workflow for comparing two LaTeX files in a compiled PDF.



NumPy Search
------------

![](screenshots/np.tiff)

**np "method name"**

Search the methods in the NumPy module, and see a short description from the docstring. Actioning the item opens the documentation for the method in your browser.  Useful if you can't quite remember the name of one of the methods (e.g, atan or arctan), or if can't remember the order of the arguments for one of the methods and want to pull it up in your browser.  Currently, NumPy Search only includes methods that are directly in the numpy module and not in submodules (e.g., numpy.polynomial or numpy.linalg)

**scrapenp**

The workflow contains a cached version of the relevant information from the NumPy docs.  If NumPy is updated and the local cache is out of date, you can run "scrapenp" to redownload the relevant data.  Be patient though, as it will take a few minutes.  A notification will pop-up when its complete.

#### [[Download NumPy Search Workflow](https://github.com/andrewning/alfred-workflows-scientific/raw/master/numpy-search/NumPy%20Search.alfredworkflow)]



Citation Search
---------------

![](screenshots/cite.tiff)

**cite "citation metadata"**

A search api (beta) provided by [CrossRef](http://search.labs.crossref.org) attempts to match your provided citation metadata.  You can search using any part of a citation (e.g., author names, article title, digital object identifier (DOI), etc.), or even a full citation.  It then grabs the associated BibTeX reference from the [International DOI Foundation](http://dx.doi.org) (IDF).  If you have the application [BibDesk](http://bibdesk.sourceforge.net) and one of its documents is open (or if you've set the preference in BibDesk to open a file at application launch), the BibTex entry will be directly imported.  For those that don't use BibDesk, the BibTeX reference is also copied to the clipboard.  Obviously the article you're interested in needs to have a registered DOI with IDF (generally only journal articles).  Occasionaly some articles don't have associated BibTeX data stored with them, and a "Not Available" notification will be posted.

**cite "citation metadata" [cmd]**

Hold down [cmd] when actioning an article to go to the landing page associated with the article.  If you have a subscription to the associated journal you can then access the PDF.

**cite "citation metadata" [alt]**

Hold down [alt] \(option) when actioning an article to copy a formatted reference to the clipboard.  Theoretically the API used by doi.org should allow you to format the reference using any style in the [Citation Style Language](https://github.com/citation-style-language/styles) database.  However, in practice I've found that the vast majority are not working.  For now, until a better solution can be found, the formatted reference is in APA format.

**cite "doi"!!**

I've noticed that for some recently added papers the DOI information will be registered with doi.org, but the data is not yet indexed by the CrossRef search engine.  If you do have the DOI, there is no need for going through CrossRef anyway and you can just grab the relevant citation data directly.  Just add a double bang (two exclamation marks) after the DOI to bypass the metadata search.  (This option also works will the [cmd] and [alt] modifiers).




#### [[Download Citation Search Workflow](https://github.com/andrewning/alfred-workflows-scientific/raw/master/citation-search/Citation%20Search.alfredworkflow)]



AIAA Search
-----------

![](screenshots/aiaa.tiff)

**aiaa "citation info"**

Similar to BibTeX Grab, but specifically designed for searching for papers published with [The American Institute of Aeronautics and Astronautics](http://arc.aiaa.org) (AIAA).  If you're looking for an AIAA paper, this workflow is definitely preferrable to BibTeX Grab, as it contains all published AIAA papers (conference or journal).  There is no official API for this, so performance is a bit slower.  If a [BibDesk](http://bibdesk.sourceforge.net) document is open (or if you've set the preference in BibDesk to open a file at application launch), the BibTex entry will be directly imported.  For those that don't use BibDesk, the BibTeX reference is also copied to the clipboard.

**aiaa "citation info" [cmd]**

If you hold down [cmd] when actioning an article, the PDF will be downloaded directly from AIAA (an AIAA subscription is required only for the PDF download functionality).

#### [[Download AIAA Search Workflow](https://github.com/andrewning/alfred-workflows-scientific/raw/master/aiaa-search/AIAA%20Search.alfredworkflow)]


LaTeX Tools
-----------

![](screenshots/texcount.tiff)

**texcount "tex file"**

Parses LaTeX file to do a word count using the Perl script [texcount.pl](http://app.uio.no/ifi/texcount/).  Reports back a concise summary on the number of words (text, headers, and captions), number of floats, and number of displayed equations (not counting inline equations).  Depending on the journal of interest you can then convert the floats/equations to equivalent word counts.

![](screenshots/texdiff.tiff)

**TeXDiff [file action]**  *(alpha)*

TexDiff is a file action to compare two LaTeX files using the Perl script [latexdiff.pl](http://www.ctan.org/pkg/latexdiff).  Add the files to Alfred's Temporary File Buffer (⌥↑ by default) then action the items in the buffer (⌥→ by default).  The shell script will then recursively copy both directories in which the files are contained (in order to get associated images, BibTeX files, etc.), run latexdiff.pl, run latexmk to build a pdf, and then open the pdf showing the difference between the files.  This workflow requires that you have MacTeX installed (more specifically you need latexmk and pdflatex in /usr/texbin).  This workflow should be considered in alpha status.  If you don't see a PDF open up within a minute, then there was likely an error with the pdf building process.  Open the workflow folder and check output.log.  If reliability becomes a common problem, the workflow may be reduced to stop at building the diff.tex file and leave the final compilation to pdf to the user.

#### [[Download LaTeX Tools Workflow](https://github.com/andrewning/alfred-workflows-scientific/raw/master/latex-tools/LaTeX%20Tools.alfredworkflow)]



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
