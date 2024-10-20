# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import os # Incluido
import sys # Incluido
sys.path.insert(0, os.path.abspath('../..')) # Incluido

project = 'Docs'
copyright = '2024, ITMSS'
author = 'ITMSS'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc", # Incluido
    "sphinx.ext.napoleon", # Incluido
    "sphinx_autodoc_typehints", # Incluido
    "sphinx.ext.viewcode",  # Incluido

]

templates_path = ['_templates']
exclude_patterns = [
    "migrations/*", # Incluido
    "*/admin.py", # Incluido
    "*/apps.py",    # Incluido
    "*/models.py", # Incluido
    "*/urls.py", # Incluido
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster' Padrao
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

autodoc_mock_imports = [
    "django.contrib.admin",
    "django.apps",
    "django.db.migrations"
]