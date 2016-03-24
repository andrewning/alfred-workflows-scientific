alfred-workflows-scientific
===========================

A collection of [Alfred v2](http://www.alfredapp.com) workflows targeting scientific applications.  Use of workflows requires the Alfred PowerPack.

- [Reference Importer](#reference-importer): search for an article/book from a variety of sources and import the corresponding reference data (BibTex, PDF) into BibDesk, copy BibTeX to clipboard, go to the landing page for the article, or copy a formatted reference.  Also supports reference lookup from a PDF file. (This workflow was formerly known as "Citation Search" and "AIAA Search")
- [Go To Current File](#go-to-current-file): Keyboard shortcut to quickly go to the file in the frontmost app (either in Finder, Terminal, iTerm2, or Alfred's File Action Window).
- [NumPy Search](#numpy-search): search methods within the NumPy module and open the associated documentation in your browser.
- [LaTeX Tools](#latex-tools): tools for working with LaTeX files.  Currently a word/figure/equation count, and a diff workflow for comparing two LaTeX files in a compiled PDF.


## Reference Importer

#### [[Download Reference Importer Workflow](https://github.com/andrewning/alfred-workflows-scientific/raw/master/reference-importer/Reference%20Importer.alfredworkflow)]


This workflow is a combination of two of my former workflows (Citation Search and AIAA Search) with many improvements and new features.  It allows you to import BibTeX, and in some cases a linked PDF, for:

- journal articles through a CrossRef DOI lookup
- books thorough Google Books
- journal and conference papers through Google Scholar search
- a PDF on your computer by scanning the PDF for its DOI and then going through CrossRef
- AIAA journal and conference papers (these are now available through CrossRef so the separate AIAA functionality was removed)

This workflow is primarily intended to work with [BibDesk](http://bibdesk.sourceforge.net), but it also copies the BibTeX to the clipboard so it can be used with other applications.  If you do use BibDesk it is recommended that you set the preference in BibDesk to open a certain file at application launch.  Otherwise, you will need to have the BibDesk document open that you want to import to before running the workflow.

### ref "search terms"

![](screenshots/ref.tiff)


A search api (beta) provided by [CrossRef](http://search.labs.crossref.org) attempts to match your provided citation metadata.  You can search using any part of a citation (e.g., author names, article title, digital object identifier (DOI), etc.), or even a full citation.  The workflow then grabs the associated BibTeX reference from CrossRef.  Obviously the article you're interested in needs to have a registered DOI (generally only applies to journal articles).  Occasionaly some articles don't have associated BibTeX data stored with them, and a "Not Available" notification will be posted.

For certain journals (currently only [Wind Energy][1], because that's what I happen to use) the PDF will also be automatically downloaded (if you have a subscription to the journal) and linked to your BibDesk entry.  Unfortunately there is no universal way to automatically get the PDF because every journal uses a different link format, but I provide hooks in the script to allow addition of other journals.  Or the workflow can take you to the article's landing page as discussed below, and you can manually download the PDF.

### ref "search terms" \[cmd\]

Hold down [cmd] when actioning an article to go to the landing page associated with the article.  If you have a subscription to the associated journal you can then access the PDF.

### ref "search terms" \[alt\]

Hold down alt \(option) when actioning an article to copy a formatted reference to the clipboard.  Theoretically the API used by CrossRef should allow you to format the reference using any style in the [Citation Style Language](https://github.com/citation-style-language/styles) database.  However, in practice I've found that the vast majority are not working.  For now, until a better solution can be found, the formatted reference is in APA format.

### ref "doi"!!

I've noticed that for some recently added papers the DOI information will be registered, but the data is not yet indexed by the CrossRef search engine.  If you do have the DOI, you can bypass the search and attempt to just grab the relevant citation data directly.  Just add a double bang (two exclamation marks) after the DOI to bypass the metadata search.  (This option also works will the [cmd] and [alt] modifiers).

### book "search terms"

![](screenshots/book.tiff)

Uses Google Books API to search the Google books repository.  Selecting a book will import corresponding BibTeX into BibDesk and copy the BibTeX to the clipboard.

### gsref "search terms".  (note the period)

![](screenshots/gs.tiff)

Searches Google Scholar for relevant journal/conference papers, imports the associated BibTeX, and if a PDF is available will also download the PDF and link it to the corresponding BibDesk entry.  I've disabled search as you type for this particular query, because Google Scholar will block you for the day if you send searches too rapidly and it thinks you are a bot.  When your query is complete, add a period "." to the end in order to actually trigger the search.

### Keyboard Shortcut or File Action

You can select a PDF in Finder and press a custom keyboard shortcut, or use a file action on an PDF to try to get the associated BibTeX.  The script will scan the first page of the PDF, and will attempt to find a DOI.  If it cannot find a valid DOI, it will grab the first dozen capitalized words.  In either case, it will use those terms (DOI, or capitalized words) to initiate the [CrossRef search from above](#ref-search-terms).  The search will not be immediately executed so you can still modify the search terms to your liking.  Additionally, the location of the PDF will be remembered so that it will be automatically linked to the new BibTeX entry.


#### [[Download Reference Importer Workflow](https://github.com/andrewning/alfred-workflows-scientific/raw/master/reference-importer/Reference%20Importer.alfredworkflow)]


[1]: http://onlinelibrary.wiley.com/journal/10.1002/(ISSN)1099-1824

#### Acknowledgments

The following packages/codes are used within this workflows:

- [Requests](http://docs.python-requests.org/en/latest/), an HTTP library written in Python.
- [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/), a Python library for parsing HTML
- [pdftotext](http://www.foolabs.com/xpdf/download.html)
- [alfred-python](https://github.com/nikipore/alfred-python), a lightweight wrapper to Alfred's workflow API



Go To Current File
------------------

#### [[Download Go To Current File Workflow](https://github.com/andrewning/alfred-workflows-scientific/raw/master/goto-file/Go%20To%20Current%20File.alfredworkflow)]

Allows you to assign a keyboard shortcut to quickly go to the current file in Finder, Terminal (or iTerm2), or Alfred's File Action Window.  For example, you are working on a presentation in Keynote and want to go to the corresponding directory.  You could right click on the title of the file in the menu bar and then click in the folder (plus an additional step if you want to get to the terminal), or just hit a keyboard shortcut and go right there.

This may not necessarily work for all applications---some are not file-based so it wouldn't make sense, and some use non-standard properties.  It should definitely work for apps that follow standard AppleScript conventions: iWork (Keynote, Pages, Numbers), Preview, Skim, BibDesk, Byword, MS Office (PowerPoint, Word, Excel), Marked, etc..  It has a fall-back method for those apps that don't provide an AppleScript Dictionary or are non-standard (Sublime Text).  If you come across an app this doesn't work for, let me know and I'll see if it's possible to add.

**Note for Microsoft Office users**: 

Microsoft Office doesn't follow standard AppleScript.  To prevent the script from throwing errors from those who did not use MS Office, I left this functionality out by default.  You should download [this version](https://github.com/andrewning/alfred-workflows-scientific/raw/master/goto-file/Go%20To%20Current%20File%20MS.alfredworkflow) instead.  The only difference is each "Run Script" adds the key phrase MS at the end which lets the script know its OK to check for MS Office files in addition to all the others.

**Note on Terminal/iTerm2**: 

If you don't use iTerm2, don't set the third keyboard shortcut.  That one is only for iTerm.

**Note for Mavericks users**: 

If it does not work for certain applications, make sure you have given Alfred permission to control the computer through the Accessibility pane in the Security & Privacy settings of OS X preferences.


#### [[Download Go To Current File Workflow](https://github.com/andrewning/alfred-workflows-scientific/raw/master/goto-file/Go%20To%20Current%20File.alfredworkflow)]


NumPy Search
------------

#### [[Download NumPy Search Workflow](https://github.com/andrewning/alfred-workflows-scientific/raw/master/numpy-search/NumPy%20Search.alfredworkflow)]

![](screenshots/np.tiff)

**np "method name"**

Search the methods in the NumPy module, and see a short description from the docstring. Actioning the item opens the documentation for the method in your browser.  Useful if you can't quite remember the name of one of the methods (e.g, atan or arctan), or if can't remember the order of the arguments for one of the methods and want to pull it up in your browser.  Currently, NumPy Search only includes methods that are directly in the numpy module and not in submodules (e.g., numpy.polynomial or numpy.linalg)

**scrapenp**

The workflow contains a cached version of the relevant information from the NumPy docs.  If NumPy is updated and the local cache is out of date, you can run "scrapenp" to redownload the relevant data.  Be patient though, as it will take a few minutes.  A notification will pop-up when its complete.

#### [[Download NumPy Search Workflow](https://github.com/andrewning/alfred-workflows-scientific/raw/master/numpy-search/NumPy%20Search.alfredworkflow)]










LaTeX Tools
-----------

#### [[Download LaTeX Tools Workflow](https://github.com/andrewning/alfred-workflows-scientific/raw/master/latex-tools/LaTeX%20Tools.alfredworkflow)]

![](screenshots/texcount.tiff)

**texcount "tex file"**

Parses LaTeX file to do a word count using the Perl script [texcount.pl](http://app.uio.no/ifi/texcount/).  Reports back a concise summary on the number of words (text, headers, and captions), number of floats, and number of displayed equations (not counting inline equations).  Depending on the journal of interest you can then convert the floats/equations to equivalent word counts.

![](screenshots/texdiff.tiff)

**TeXDiff [file action]**  *(alpha)*

TexDiff is a file action to compare two LaTeX files using the Perl script [latexdiff.pl](http://www.ctan.org/pkg/latexdiff).  Add the files to Alfred's Temporary File Buffer (⌥↑ by default) then action the items in the buffer (⌥→ by default).  The shell script will then recursively copy both directories in which the files are contained (in order to get associated images, BibTeX files, etc.), run latexdiff.pl, run latexmk to build a pdf, and then open the pdf showing the difference between the files.  This workflow requires that you have MacTeX installed (more specifically you need latexmk and pdflatex in /usr/texbin).  This workflow should be considered in alpha status.  If you don't see a PDF open up within a minute, then there was likely an error with the pdf building process.  Open the workflow folder and check output.log.  If reliability becomes a common problem, the workflow may be reduced to stop at building the diff.tex file and leave the final compilation to pdf to the user.

#### [[Download LaTeX Tools Workflow](https://github.com/andrewning/alfred-workflows-scientific/raw/master/latex-tools/LaTeX%20Tools.alfredworkflow)]





License
-------

Copyright (c) 2013, S. Andrew Ning.  All rights reserved.

All code is licensed under [The MIT License](http://opensource.org/licenses/mit-license.php).

