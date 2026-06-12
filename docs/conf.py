# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'solarbench'
copyright = '2024-26, solarbench team'
author = 'solarbench team'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx_favicon',
    'jupyter_sphinx']

templates_path = ['_templates']
exclude_patterns = ['_build', 
                    'Thumbs.db', 
                    '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
# html_theme = 'alabaster'
html_static_path = ['_static']

html_show_sourcelink = False

html_theme_options = {
  "github_url": "https://github.com/Solar4cast/solarbench_readthedocs",
  "show_nav_level": 1,
  "navigation_depth": 3,
  "show_toc_level": 1,
  "show_prev_next": False,
  "logo": {
      "text": "solarbench",
      "image_light": "_static/favicon.webp",
      "image_dark": "_static/favicon.webp",
  }
}

# ----- Options for Napoleon -------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# ------ Other options ------------------------
autosummary_generate = True
autodoc_mock_imports = ["datasets", "os", "json"]
# skips = ["temporal_distortion_metrics"]
skips = []

def skip(app, what, name, obj, would_skip, options):
    # print(name)
    if name in skips:
        print("Skipping", name)
        return True
    return would_skip

def setup(app):
    app.connect("autodoc-skip-member", skip)

favicons = [
    "favicon.webp"
]