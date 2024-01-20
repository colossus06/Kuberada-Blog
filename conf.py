# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


# def setup(app):
#     # (create a setup() function if you don't already have one;
#     # or add to the existing setup() ...)

html_title = 'Kuberada Blog'

project = 'kuberada-Hands-on Learning'
# copyright = '2024, kuberada'
author = 'kuberada'
# release = '2024'




extensions = [ 
    "myst_parser",
    "sphinxext.opengraph",
    "sphinx_design"
]


# -- Project information
copyright = "2024, Kuberada"
author = "Gulcan Topcu"
ogp_site_url = "https://devtechops.dev/"
ogp_type = "article"
ogp_image = "https://raw.githubusercontent.com/colossus06/kuberada-blog/main/og/kuberada.png"


templates_path = ['_templates']

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*import_posts*",
    "**/pandoc_ipynb/inputs/*",
    "README.md",
    "**/.ipynb_checkpoints/*",
    "docs",
]
source_suffix = ['.rst', '.md']

html_favicon = 'images/favicon.png'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

copyright = "2024, kuberada"

# html_logo= "images/kuberada.png"

# html_additional_pages = {"index": "your-custom-landing-page.html"}

html_theme = 'furo'
html_static_path = ['_static']

html_css_files = ["css/custom.css"]

# pygments_style = "sphinx"
# pygments_dark_style = "monokai"


html_theme_options = {
    "top_of_page_button": "None",
    'navigation_with_keys': True,
    "announcement": "Kuberada 💛 Hands-on Only 🏭",
    "light_css_variables": {
        # "font-stack": "Ubuntu, sans-serif",
        # "font-stack--monospace": "Oswald, monospace",
        "color-brand-primary": "#21209C",
        "color-brand-content": "#FF8400"
    },
    "dark_css_variables": {
        # "font-stack": "Ubuntu, sans-serif",
        # "font-stack--monospace": "Oswald, monospace",
        "color-brand-primary": "#FFED00",
        "color-brand-content": "#10CD23"
    },
}

html_js_files = [
    'js/activate.js',
    'js/react.js',
    'js/share.js',
    'js/joke.js'
]

# These are options specifically for the Wagtail Theme.
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
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