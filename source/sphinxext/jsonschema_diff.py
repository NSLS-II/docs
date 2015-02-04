#
# based on
# https://github.com/spacetelescope/understanding-json-schema/blob/master/source/sphinxext/jsonschemaext.py
#
# Copyright (c) 2013, Space Telescope Science Institute
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#   Neither the name of the Space Telescope Science Institute nor the
#   names of its contributors may be used to endorse or promote products
#   derived from this software without specific prior written
#   permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

import json

from docutils import nodes
from docutils import statemachine
from sphinx.util.compat import Directive
from sphinx.util.nodes import set_source_info

import jsonschema


class jsonschema_node(nodes.Element):
    pass


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def split_content(l):
    parts = []
    should_pass = True
    part = []
    comment = []

    def add_part():
        content = '\n'.join(part)
        try:
            json_content = json.loads(content)
        except ValueError:
            if should_pass:
                raise ValueError("Invalid json: {0}".format(content))
            else:
                # A complex number will never validate
                json_content = 1+1j
        parts.append(AttrDict({
            'should_pass': should_pass,
            'content': content,
            'json': json_content,
            'comment': comment}))

    for line in l:
        if line.startswith('//'):
            comment.append(line[2:].lstrip())
        elif line == '--':
            add_part()
            should_pass = True
            part = []
            comment = []
        elif line == '--X':
            add_part()
            should_pass = False
            part = []
            comment = []
        else:
            part.append(line)

    add_part()

    return parts[0], parts[1:]


class SchemaExampleDirective(Directive):
    has_content = True
    validate = True

    def run(self):
        result = []

        schema, parts = split_content(self.content)

        container = jsonschema_node()
        set_source_info(self, container)
        literal = nodes.literal_block(
            schema.content, schema.content)
        literal['language'] = 'javascript'
        literal['classes'] = container['classes'] = ['jsonschema']
        set_source_info(self, literal)
        container.children.append(literal)
        result.append(container)

        for part in parts:
            if self.validate:
                is_valid = True
                try:
                    jsonschema.validate(part.json, schema.json)
                except jsonschema.ValidationError as e:
                    is_valid = False
                except jsonschema.SchemaError as e:
                    raise ValueError("Schema is invalid:\n{0}\n\n{1}".format(
                        str(e), schema.content))

                if is_valid != part.should_pass:
                    if part.should_pass:
                        raise ValueError(
                            "Doc says fragment should pass, "
                            "but it does not validate:\n" +
                            part.content)
                    else:
                        raise ValueError(
                            "Doc says fragment should not pass, "
                            "but it validates:\n" +
                            part.content)
            else:
                is_valid = part.should_pass

            if len(part.comment):
                paragraph = nodes.paragraph('', '')
                comment = statemachine.StringList(part.comment)
                comment.parent = self.content.parent
                self.state.nested_parse(comment, 0, paragraph)
                paragraph['classes'] = ['jsonschema-comment']
                set_source_info(self, paragraph)
                result.append(paragraph)

            container = jsonschema_node()
            set_source_info(self, container)
            literal = nodes.literal_block(
                part.content, part.content)
            literal['language'] = 'javascript'
            if is_valid:
                literal['classes'] = container['classes'] = ['jsonschema-pass']
            else:
                literal['classes'] = container['classes'] = ['jsonschema-fail']
            set_source_info(self, literal)
            container.children.append(literal)
            result.append(container)

        return result


class SchemaExampleNoValidationDirective(SchemaExampleDirective):
    validate = False


def visit_jsonschema_node_html(self, node):
    pass


def depart_jsonschema_node_html(self, node):
    pass


def visit_jsonschema_node_latex(self, node):
    adjust = False
    color = "gray"
    char = ""
    if 'jsonschema-pass' in node['classes']:
        char = r"\Checkmark"
        color = "ForestGreen"
        adjust = True
    elif 'jsonschema-fail' in node['classes']:
        char = r"\XSolidBrush"
        color = "BrickRed"
        adjust = True
    elif 'jsonschema' in node['classes']:
        char = r"\{ json schema \}"

    if adjust:
        self.body.append(r"\begin{adjustwidth}{2.5em}{0pt}")
    self.body.append(r"\begin{jsonframe}{%s}{%s}" % (char, color))


def depart_jsonschema_node_latex(self, node):
    adjust = False
    if 'jsonschema-pass' in node['classes']:
        adjust = True
    elif 'jsonschema-fail' in node['classes']:
        adjust = True

    self.body.append(r"\end{jsonframe}")
    if adjust:
        self.body.append(r"\end{adjustwidth}")


def setup(app):
    app.add_directive('schema_example', SchemaExampleDirective)
    app.add_directive('schema_example_novalid',
                      SchemaExampleNoValidationDirective)

    app.add_node(jsonschema_node,
                 html=(visit_jsonschema_node_html, depart_jsonschema_node_html),
                 latex=(visit_jsonschema_node_latex, depart_jsonschema_node_latex))


latex_preamble = r"""
\usepackage{changepage}
\usepackage[dvipsnames]{xcolor}
"""
