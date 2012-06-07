from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/layout/layout_base.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/base_web.html', '/source/layout/layout_base.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_header(context, environment=environment):
        if 0: yield None
        yield u'\n<nav role="navigation">\n\t<ul class=\'right\'>\n\t\t\n\t\t<li><a href="/signup" title="Sign Up">Sign Up</a></li>\n\t\t<li><a href="/login" title="Log In">Log In</a></li>\n\t</ul>\n</nav>\n'

    def block_main(context, environment=environment):
        if 0: yield None
        yield u'\n'

    def block_footerleft(context, environment=environment):
        if 0: yield None
        yield u"\n\t\t<div class='left'>\n\t        BETA - work in progress\n\t    </div>\n    "

    def block_footerright(context, environment=environment):
        if 0: yield None
        yield u"\n\t\t<div class='right'>\n\t        copyright (c) 2012, openfire\n\t    </div>\n    "

    def block_footer(context, environment=environment):
        if 0: yield None
        yield u"\n    <div id='footer-content'>\n    "
        for event in context.blocks['footerleft'][0](context):
            yield event
        yield u'\n\n    '
        for event in context.blocks['footerright'][0](context):
            yield event
        yield u'\n    </div>\n'

    blocks = {'header': block_header, 'main': block_main, 'footerleft': block_footerleft, 'footerright': block_footerright, 'footer': block_footer}
    debug_info = '1=9&3=15&13=19&18=23&24=27&16=31&18=34&24=37'
    return locals()