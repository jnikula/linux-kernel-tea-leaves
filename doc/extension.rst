.. SPDX-License-Identifier: AGPL-3.0-or-later
.. SPDX-FileCopyrightText: 2025 Jani Nikula <jani@nikula.org>

=========
Extension
=========

The Linux Kernel Tea Leaves is now a Sphinx extension you can embed in your own
documentation.

Installation
============

It's in the repository. I'm afraid you'll have to figure it out by yourself.

You'll need to also copy the template from this project's Sphinx template
directory, or create your own.

Configuration
=============

.. py:data:: linux_kernel_tea_leaves_template
   :type: str

   Name of the template within the Sphinx template directory. Defaults to
   ``tealeaves.rst``.

.. py:data:: linux_kernel_tea_leaves_releases
   :type: int

   Number of kernel release cycles to predict. Defaults to 3.

Directive
=========

.. rst:directive:: .. tealeaves::

   Directive to embed predictions in the current document.

   .. rst:directive:option:: template
      :type: text

      Name of the template within the Sphinx template directory. Defaults to
      :data:`linux_kernel_tea_leaves_template`

   .. rst:directive:option:: format
      :type: text

      Template format, either ``rst`` or ``html``. Defaults to ``rst`` if the
      name of the template ends in ``.rst`` or ``.rest``, ``html`` otherwise.

   .. rst:directive:option:: releases
      :type: int

      Number of kernel release cycles to predict. Defaults to
      :data:`linux_kernel_tea_leaves_releases`.

   .. rst:directive:option:: tag
      :type: text

      Tag to use for reference instead of fetching the latest tag from the
      upstream repository. Primarily for testing purposes.

   .. rst:directive:option:: date
      :type: text

      Date to use for the tag instead of fetching the tag date from the upstream
      repository. Primarily for testing purposes.
