from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/core/__north.html'

    def root(context, environment=environment):
        l_asset = context.resolve('asset')
        l_page = context.resolve('page')
        if 0: yield None
        yield u'<!-- Stylesheets -->\n<style>@import url(http://fonts.googleapis.com/css?family=Satisfy);</style>\n<link rel="stylesheet" href="%s">\n\n' % (
            context.call(environment.getattr(l_asset, 'style'), 'main', 'compiled'), 
        )
        if environment.getattr(l_page, 'ie'):
            if 0: yield None
            yield u'\n\t<link rel="stylesheet" href="%s">\n' % (
                context.call(environment.getattr(l_asset, 'style'), 'ie', 'compiled'), 
            )

    blocks = {}
    debug_info = '3=11&5=13&6=16'
    return locals()