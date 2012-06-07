from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/layout/landing.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layout/layout_base.html', '/source/layout/landing.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content(context, environment=environment):
        if 0: yield None
        yield u"\n\t\t\t<section id='projects' class='cardstack' role='region'>\n\t\t        "
        for event in context.blocks['projects'][0](context):
            yield event
        yield u"\n\t\t    </section><!-- #projects -->\n\n\t\t    <section id='activity' class='newsfeed' role='region'>\n\t\t        "
        for event in context.blocks['activity'][0](context):
            yield event
        yield u'\n\t\t    </section><!-- #activity -->\n\t\t '

    def block_masthead(context, environment=environment):
        if 0: yield None
        yield u'\n\t        <img src=\'https://d2ipw8y1masjpy.cloudfront.net/static/branding/openfire_transparent_optimized.png\' alt=\'openfire!\' width=\'600\' height=\'173\' />\n\t        <h1 id="title"><span class=\'lightorange\'>momentum for</span> <span class=\'darkorange\'>positive disruption</span></h1>\n\t    '

    def block_main(context, environment=environment):
        if 0: yield None
        yield u"\n\n\t<!-- Main Masthead -->\n\t<div id='masthead'>\n\t    "
        for event in context.blocks['masthead'][0](context):
            yield event
        yield u"\n\t</div><!-- #masthead -->\n\n    <div id='content'>\n\t\t"
        for event in context.blocks['content'][0](context):
            yield event
        yield u'\n\t </div><!-- #content -->\n\n'

    def block_projects(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t        <h2>Projects</h2>\n\t\t        <hr />\n\t\t        '

    def block_activity(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t        <h2>Activity</h2>\n\t\t        <hr />\n\t\t        '

    blocks = {'content': block_content, 'masthead': block_masthead, 'main': block_main, 'projects': block_projects, 'activity': block_activity}
    debug_info = '1=9&14=15&16=18&23=21&7=25&3=29&7=32&14=35&16=39&23=43'
    return locals()