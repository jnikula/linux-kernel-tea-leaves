# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2025 Jani Nikula <jani@nikula.org>
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / 'src'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LKTL'
copyright = '2025, Jani Nikula'
author = 'Jani Nikula'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['tealeaves']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_theme_options = {
    'description': 'The Linux Kernel Tea Leaves',
    'extra_nav_links': {
        'GitHub': 'https://github.com/jnikula/linux-kernel-tea-leaves',
    },
    'sidebar_width': '280px',
    'page_width': '1000px',
}

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
    ]
}

# -- Options for Linux Kernel Tea Leaves --------------------------------------
#linux_kernel_tea_leaves_template = 'tealeaves.rst'
#linux_kernel_tea_leaves_releases = 3
