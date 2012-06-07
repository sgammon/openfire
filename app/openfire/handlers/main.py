# -*- coding: utf-8 -*-
from openfire.handlers import WebHandler


class Landing(WebHandler):

    ''' openfire landing page. '''

    def get(self):

        ''' Render landing.html or landing_noauth.html. '''

        # TODO: How to determine logged in?
        if False:
            self.render('main/landing_noauth.html')
        else:
            self.render('main/landing.html')
        return
