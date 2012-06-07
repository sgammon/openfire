from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/layout/project.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layout/layout_base.html', '/source/layout/project.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_media(context, environment=environment):
        if 0: yield None
        yield u'\n        <div>\n          <h1>openfire project MEDIA</h1>\n        </div>\n    '

    def block_main(context, environment=environment):
        if 0: yield None
        yield u'\n\n    '
        for event in context.blocks['right'][0](context):
            yield event
        yield u'\n\n    '
        for event in context.blocks['media'][0](context):
            yield event
        yield u'\n\n    '
        for event in context.blocks['description'][0](context):
            yield event
        yield u'\n\n'

    def block_right(context, environment=environment):
        if 0: yield None
        yield u'\n        <div>\n          <h1>openfire project RIGHT</h1>\n        </div>\n    '

    def block_description(context, environment=environment):
        if 0: yield None
        yield u'\n        <div>\n          <h1>openfire project DESCRIPTION</h1>\n        </div>\n    '

    blocks = {'media': block_media, 'main': block_main, 'right': block_right, 'description': block_description}
    debug_info = '1=9&11=15&3=19&5=22&11=25&17=28&5=32&17=36'
    return locals()