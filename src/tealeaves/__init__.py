# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2025 Jani Nikula <jani@nikula.org>

import pathlib

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import ViewList
from sphinx.util.docutils import switch_source_input, SphinxDirective
from sphinx.util.nodes import nested_parse_with_titles

from tealeaves import fetch, predict

def template_format(fmt):
    return directives.choice(fmt, ('rst', 'html'))

class LinuxKernelTeaLeaves(SphinxDirective):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False

    option_spec = {
        'template': directives.unchanged,
        'format': template_format,
        'releases': int,
        'tag': directives.unchanged,
        'date': directives.unchanged,
    }

    @staticmethod
    def default_format(name):
        p = pathlib.Path(name)
        suffix = p.suffix[1:] if p.suffix else ''

        if suffix in ['rst', 'rest']:
            return 'rst'
        else:
            return 'html'

    def run(self):
        # options
        template_name = self.options.get('template', self.env.config.linux_kernel_tea_leaves_template)
        template_format = self.options.get('format', self.default_format(template_name))
        num_releases = self.options.get('releases', self.env.config.linux_kernel_tea_leaves_releases)
        tag = self.options.get('tag', fetch.get_latest_tag())
        date = self.options.get('date', fetch.get_tag_date(tag))

        # get the reference and predictions
        reference_tag, tags = predict.predict(tag, date, num_releases)

        # render template with context
        render = self.env.app.builder.templates.render(template_name, {
            'reference_tag': reference_tag,
            'tags': tags,
        })

        if template_format == 'rst':
            viewlist = ViewList()
            for i, line in enumerate(render.splitlines()):
                viewlist.append(line, template_name, i)

            with switch_source_input(self.state, viewlist):
                node = nodes.section()
                nested_parse_with_titles(self.state, viewlist, node)

            result = node.children

        else:
            result = [nodes.raw('', render, format='html')]

        return result

def setup(app):
    app.add_directive('linux-kernel-tea-leaves', LinuxKernelTeaLeaves)
    app.add_config_value('linux_kernel_tea_leaves_template', 'tealeaves.rst', 'env', [str])
    app.add_config_value('linux_kernel_tea_leaves_releases', 3, 'env', [int])

    return {
        'version': '0.1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
