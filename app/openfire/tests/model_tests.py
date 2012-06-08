# -*- coding: utf-8 -*-
"""
Model tests.
"""
from google.appengine.dist import use_library
use_library('django', '1.2')

import unittest
#from google.appengine.ext import db
#from google.appengine.api import memcache
from google.appengine.ext import testbed

from openfire.models.project import Category

class CategoryTestCase(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def testInsertEntity(self):
        Category(
            slug="test",
            name="Test Category",
            description="some txt here",
            ).put(use_memcache=False)
        self.assertEqual(1, len(Category.query().fetch(2)))
