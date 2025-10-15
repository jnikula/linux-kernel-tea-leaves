{# SPDX-License-Identifier: AGPL-3.0-or-later #}
{# SPDX-FileCopyrightText: 2025 Jani Nikula <jani@nikula.org> #}

Based on
`{{ reference_tag.tag }} <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tag/?h={{ reference_tag.tag }}>`_
having been tagged on {{ reference_tag.date }}, the tea leaves say:

{% for tag in tags[1:] %}

{% if tag.is_rc(1) %}
{% set title = tag.development_cycle ~ " development cycle" %}
{{ title }}
{{ "-" * title|length }}

  *Merge window for features heading to {{ tag.development_cycle }}*

{% endif %}

{% if tag.is_prediction %}
{{ tag.tag }} {{ 'release' if tag.is_release }} predicted {{ tag.date }}
{% else %}
`{{ tag.tag }} <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tag/?h={{ tag.tag }}>`_ {{ tag.date }}
{% endif %}

{% if tag.is_rc(5) %}
  *The drm subsystem deadline for features heading to {{ tag.next_development_cycle }} release.*
{% endif %}

{% endfor %}
