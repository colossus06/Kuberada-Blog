# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

html_title = 'Kuberada Blog'

project = 'kuberada-Hands-on Learning'
# copyright = '2024, kuberada'
author = 'kuberada'
# release = '2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [ 
    "myst_parser"        
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = ['.rst', '.md']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

copyright = "2024, kuberada"

html_logo= "images/kuberada.png"

html_css_files = ["custom.css"]

html_theme = 'furo'
html_static_path = ['_static']

html_theme_options = {
    'navigation_with_keys': True,
}

# These are options specifically for the Wagtail Theme.
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]


html_context = {
    "display_github": False, # Add 'Edit on Github' link instead of 'View page source'
    "last_updated": False,
    "commit": False,
    "default_mode": "light"
}

html_show_sourcelink = False

html_show_sphinx = False
master_doc = 'index'



