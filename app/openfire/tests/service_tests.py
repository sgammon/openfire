# -*- coding: utf-8 -*-
"""
Service tests.
"""
from google.appengine.dist import use_library
use_library('django', '1.2')

import unittest
from google.appengine.ext import testbed

import bootstrap
bootstrap.AppBootstrapper.prepareImports()
from apptools import dispatch

import webapp2
import json
import copy

import test_db_loader as db_loader


API_DICT = {
    'id':1,
    'opts':{},
    'agent':{},
    'request': {
        'params': {},
        'method':'echo',
        'api':'system',
    },
}


def generic_service_method_success_test(test_case, service_name, service_method, params={}):
    ''' A generic success test for a given service url.
    Returns a response dict loaded from the response body with json.
    '''

    requestDict = copy.deepcopy(API_DICT)
    requestDict['request']['api'] = service_name
    requestDict['request']['method'] = service_method
    requestDict['request']['params'] = params
    request = webapp2.Request.blank('/_api/rpc/%s.%s' % (service_name, service_method))
    request.headers['content-type'] = 'application/json'
    request.method = 'POST'
    request.body = json.dumps(requestDict)
    response = request.get_response(dispatch.gateway)
    test_case.assertEqual(response.status_int, 200)
    test_case.assertTrue(len(response.body))
    responseDict = json.loads(response.body)
    test_case.assertTrue(responseDict)
    return responseDict


class SystemServiceTestCase(unittest.TestCase):
    ''' Test cases for user services.
    '''

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()

    def test_echo_service_method(self):
        message_content = 'TESTING'
        echoParams = {'message': message_content}
        response = generic_service_method_success_test(self, 'system', 'echo', params=echoParams)
        self.assertEqual(response['response']['content']['message'], message_content, 'System echo service method failed.')

    def test_hello_service_method(self):
        response = generic_service_method_success_test(self, 'system', 'hello')
        self.assertTrue(response['response']['content']['message'].startswith('Hello'), 'System hello service failed.')


class ProjectServiceTestCase(unittest.TestCase):
    ''' Test cases for the project service.
    '''

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()

    def test_project_list_method(self):
        ''' Add one private and one public project to the database then query. '''
        db_loader.create_project(slug='test-1')
        db_loader.create_project(slug='test-2', status='p')
        response = generic_service_method_success_test(self, 'project', 'list')
        self.assertEqual(response['response']['type'], 'Projects',
            'System project list service method failed.')
        self.assertEqual(len(response['response']['content']['projects']), 1,
            'Failed to return the correct number of projects.')

    def test_project_get_method(self):
        ''' Add one private and one public project to the database then query. '''
        project_id = 'test-1'
        db_loader.create_project(slug=project_id)
        response = generic_service_method_success_test(self, 'project', 'get', params={'project_id':project_id})
        self.assertEqual(response['response']['type'], 'Project',
            'Project get service method failed.')
        self.assertEqual(response['response']['content']['slug'], project_id,
            'Project get method returned the wrong project.')

    """
    " We will fill in these tests as the service methods are implemented.
    "

    def test_project_put_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'put', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')

    def test_project_comment_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'comment', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')

    def test_project_comments_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'comments', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')

    def test_project_post_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'post', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')

    def test_project_posts_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'posts', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')

    def test_project_media_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'media', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')

    def test_project_add_media_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'add_medai', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')

    def test_project_follow_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'follow', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')

    def test_project_followers_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'followers', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')

    def test_project_backers_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'backers', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')

    def test_project_back_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'back', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')

    def test_project_suspend_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'suspend', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')

    def test_project_shutdown_method(self):
        ''' Test something. '''
        response = generic_service_method_success_test(self, 'project', 'shutdown', params={})
        self.assertEqual(response['response']['type'], '',
            'Project  service method failed.')
    """
