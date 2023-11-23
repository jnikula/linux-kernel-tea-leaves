.. SPDX-License-Identifier: AGPL-3.0-or-later
.. Copyright (c) 2023 Jani Nikula <jani@nikula.org>

===========================
The Linux Kernel Tea Leaves
===========================

Completely accurate and trustworthy predictions of the Linux kernel releases
based on a single data point. Not.

.. contents:: Development cycles

Based on {{ reference_tag.tag }} having been tagged on {{ reference_tag.date }},
the `tea leaves`_ say:

{% for tag in tags %}
{% if tag.is_rc(1) %}
{{ tag.development_cycle }} development cycle
=============================================

  *Merge window for features heading to {{ tag.development_cycle }}*

{% endif %}
{% if tag._prediction %}
{{ tag.tag }} {{ 'release' if tag.is_release() }} predicted {{ tag.date }}
{% else %}
`{{ tag.tag }} <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tag/?h={{ tag.tag }}>`_ {{ tag.date }}
{% endif %}

{% if tag.is_rc(5) %}
  *The drm subsystem deadline for features heading to {{ tag.next_development_cycle }} release.*
{% endif %}

{% endfor %}


.. _tea leaves: https://github.com/jnikula/linux-kernel-tea-leaves
