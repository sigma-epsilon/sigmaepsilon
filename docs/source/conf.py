# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# For ideas:

# https://github.com/pradyunsg/furo/blob/main/docs/conf.py
# https://github.com/sphinx-gallery/sphinx-gallery/blob/master/doc/conf.py

# --------------------------------------------------------------------------

import sys
import os
from datetime import date

from sphinx.config import Config

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../../src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "sigmaepsilon"
copyright = "2024-%s, Bence Balogh" % date.today().year
author = "Bence Balogh"


def setup(app: Config):
    app.add_config_value("project_name", project, "html")


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx.ext.extlinks",
    "sphinx_design",
    "sphinx_inline_tabs",
]

templates_path = ["_templates"]

exclude_patterns = ["_build"]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

language = "EN"

# See warnings about bad links
nitpicky = True
nitpick_ignore = [
    ("", "Pygments lexer name 'ipython' is not known"),
    ("", "Pygments lexer name 'ipython3' is not known"),
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
pygments_dark_style = "github-dark"
highlight_language = "python3"

intersphinx_mapping = {
    "python": (r"https://docs.python.org/{.major}".format(sys.version_info), None),
    "numpy": (r"https://numpy.org/doc/stable/", None),
    "scipy": (r"https://docs.scipy.org/doc/scipy/", None),
    "awkward": (r"https://awkward-array.org/doc/main/", None),
    "matplotlib": (r"https://matplotlib.org/stable", None),
    "k3d": (r"http://k3d-jupyter.org/", None),
    "sphinx": (r"https://www.sphinx-doc.org/en/master", None),
    "pandas": (r"https://pandas.pydata.org/pandas-docs/stable/", None),
    "xarray": (r"https://docs.xarray.dev/en/stable/", None),
    "sigmaepsilon.core": (r"https://sigmaepsiloncore.readthedocs.io/en/latest/", None),
    "sigmaepsilon.math": (r"https://sigmaepsilonmath.readthedocs.io/en/latest/", None),
    "sigmaepsilon.mesh": (r"https://sigmaepsilonmesh.readthedocs.io/en/latest/", None),
    "sigmaepsilon.solid.material": (
        r"https://sigmaepsilonsolidmaterial.readthedocs.io/en/latest/",
        None,
    ),
    "sigmaepsilon.deepdict": (
        r"https://sigmaepsilondeepdict.readthedocs.io/en/latest/",
        None,
    ),
}

# sphinx_copybutton configuration --------------------------------------------

copybutton_exclude = ".linenos, .gp, .go"
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "show_prev_next": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": f"https://github.com/sigma-epsilon/{project}",
            "icon": "fab fa-github",
            "type": "fontawesome",
        },
    ],
    "logo": {
        # Because the logo is also a homepage link, including "home" in the alt text is good practice
        "text": "SigmaEpsilon",
    },
}
html_js_files = [
    "require.min.js",
    "custom.js",
]
html_css_files = ["custom.css"]
html_context = {"default_mode": "light"}
html_static_path = ["_static"]