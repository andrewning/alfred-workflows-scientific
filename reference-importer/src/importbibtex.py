#!/usr/bin/env python
# encoding: utf-8
"""
importbibtex.py

Created by Andrew Ning on 2013-11-17.
"""

from common import importBibTeXIntoBibDesk
import alfred

bibtex = alfred.args()[0]
importBibTeXIntoBibDesk(bibtex)
