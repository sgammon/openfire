# -*- coding: utf-8 -*-
from project.handlers import WebHandler


class About(WebHandler):

    ''' openfire about page. '''

    def get(self):

        ''' Render about.html. '''

        self.render('about/about.html')
        return


class Terms(WebHandler):

    ''' openfire terms page. '''

    def get(self):

        ''' Render .html. '''

        self.render('about/terms.html')
        return


class Privacy(WebHandler):

    ''' openfire privacy page. '''

    def get(self):

        ''' Render .html. '''

        self.render('about/privacy.html')
        return


class Support(WebHandler):

    ''' openfire support page. '''

    def get(self):

        ''' Render .html. '''

        self.render('about/support.html')
        return
