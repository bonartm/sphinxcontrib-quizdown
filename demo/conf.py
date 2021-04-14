# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Quizdown Demo'
copyright = '2021, Malte Bonart'
author = 'Malte Bonart'

# The full version, including alpha/beta/rc tags
release = '0.2.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.quizdown'
]

# quizdown javascript
quizdown_js='https://cdn.jsdelivr.net/gh/bonartm/quizdown-js@latest/public/build/quizdown.js'
# quizdown css
quizdown_css='https://cdn.jsdelivr.net/gh/bonartm/quizdown-js@latest/public/build/quizdown.css'
# stylesheet for syntax highlighting
quizdown_highlight_css='https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@10.6.0/build/styles/github.min.css'
# global options passed to the quizdown library
quizdown_config = {
    'start_on_load': True,			# detect and convert all divs with class quizdown
    'shuffle_answers': True,		# shuffle answers for each question
    'shuffle_questions': False,     # shuffle questsions for each quiz
    'primary_color': '#FF851B',     # primary CSS color
    'secondary_color': '#DDDDDD',   # secondary CSS color
    'title_color': 'black'          # text color of the title
}



# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']