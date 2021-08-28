# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import datetime as dt
from pathlib import Path

# import sys

# sys.path.insert(0, str(Path("..").resolve()))

from aaanimal import __version__  # noqa: E402


# -- Project information -----------------------------------------------------

changelog_mtime = Path("../CHANGELOG.rst").stat().st_mtime
copyright_year = dt.datetime.utcfromtimestamp(changelog_mtime)

project = "ipython-style-gruvbox"
author = "Reilly Tucker Siemens"
release = __version__
version = ".".join(release.split(".", 2)[:2])
copyright = f"{copyright_year:%Y}, {author}"


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_title = "Aaanimal"
