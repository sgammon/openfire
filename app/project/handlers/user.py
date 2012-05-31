# -*- coding: utf-8 -*-
from project.handlers import WebHandler


class UserLanding(WebHandler):

    ''' openfire user landing page. '''

    def get(self):

        ''' Render user_landing.html. '''

        self.render('user/user_landing.html')
        return


class UserProfile(WebHandler):

    ''' openfire user profile page. '''

    def get(self, username):

        ''' Render profile.html. '''

        self.render('user/profile.html')
        return


class UserAccount(WebHandler):

    ''' openfire user account page. '''

    def get(self, username):

        ''' Render account.html. '''

        self.render('user/account.html')
        return
