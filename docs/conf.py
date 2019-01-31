#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OLMAC PDK documentation build configuration file, created by
# Based on the documentation for lightlab (lightlab.readthedocs.io)

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
              'sphinx.ext.intersphinx',
              'sphinx.ext.inheritance_diagram',
              'sphinx.ext.coverage',
              'sphinx.ext.napoleon',
              'sphinx.ext.todo',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinxcontrib.bibtex',
              ]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']
# Program that converts .md to html
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'OLMAC PDK'
copyright = '2018 Faint Photonics Group and Quantum Nanophotonics Group, National Institute of Standards and Technology, Boulder, CO, United States'
author = 'Sonia Buckley, Adam McCaughan, Jeff Chiles, Alex Tait, Saeed Khan, Jeff Shainline, Rich Mirin, Sae Woo Nam'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

# with open("../version.py") as f:
#     code = compile(f.read(), "version.py", 'exec')
#     version_dict = {}
#     exec(code, {}, version_dict)
#     # The short X.Y version.
#     version = version_dict['version']
#     # The full version, including alpha/beta/rc tags.
#     release = version_dict['release']

import xmltodict
with open("../grain.xml") as fx:
    grain_dict = xmltodict.parse(fx.read())
version = grain_dict['salt-grain']['version']
release = version

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'venv', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
numfig = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

doc_title = 'NIST SOEN Documentation'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'OLMAC.tex', doc_title,
     author, 'manual'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ('https://docs.python.org/', None)}

# Do this conversion first
import sys, os
# import pdb; pdb.set_trace()
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
from properties2rst import convert_all
convert_all()
# def setup(app):
#     app.connect('builder-inited', convert_all)
