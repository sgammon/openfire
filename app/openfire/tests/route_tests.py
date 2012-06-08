# -*- coding: utf-8 -*-
"""
Route tests.
"""
from google.appengine.dist import use_library
use_library('django', '1.2')

import unittest
from google.appengine.ext import testbed

import bootstrap
bootstrap.AppBootstrapper.prepareImports()
from apptools import dispatch

import webapp2

class HandlerTestCase(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()

    def test_handler(self):
        request = webapp2.Request.blank('/')
        response = request.get_response(dispatch.gateway)
        self.assertEqual(response.status_int, 200)
        self.assertTrue(len(response.body))
