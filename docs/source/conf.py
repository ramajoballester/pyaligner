# Configuration file for the Sphinx documentation builder.

import os
import sys
from importlib.metadata import metadata
from datetime import datetime

# sys.path.insert(0, os.path.abspath('../../packages'))

language = 'en'

# -- Project information

project = 'pyaligner'
project_slug = project.lower()
# project_slug = 'uc3m-pic'
author = metadata(project.lower())['Author-email'].split('<')[0][:-1]
# author = 'Álvaro Ramajo'
version = metadata(project.lower())['Version']
# version = '0.1.5'
release = version
copyright = f'{datetime.now().year}, {author}'
# release = '0.1'
# version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'numpydoc',
    'sphinx.ext.autodoc.typehints',
    'myst_parser',      # For markdown support
    'sphinx.ext.autosectionlabel',
    'sphinx_tabs.tabs',
    # 'sphinx.ext.viewcode',
    'sphinx_markdown_tables',
    'sphinx.ext.napoleon',
    # 'sphinx_design'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']
templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'pytorch_sphinx_theme'
# html_theme = 'furo'
# html_theme = 'sphinx_material'



html_theme_options = {
    'prev_next_buttons_location': None,
}

# github_url = 'https://github.com/ramajoballester/sensus-loci'
# html_baseurl = 'https://sensus-loci.readthedocs.io/en/latest/'
html_favicon = '../images/favicon.ico'

html_show_sourcelink = False
# html_link_suffix = ''


# html_sidebars = {
#    '**': ['globaltoc.html', 'localtoc.html', 'searchbox.html'],
#    'using/windows': ['windowssidebar.html', 'searchbox.html'],
# }

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Configure autodoc to generate documentation for both class and module docstrings
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    # 'no-show-inheritance': True,
}

# add_module_names = False

# Set the custom template name
# html_additional_pages = {'layout': 'layout.html'}