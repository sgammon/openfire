from openfire.models.project import Project, Category
from google.appengine.ext import ndb

'''
This module is used to create database entities for testing purposes.
'''

def create_category(slug='test', name='Test Category', description='some txt'):
    return Category(key=ndb.Key('Category', slug), slug=slug, name=name, description=description,
        ).put()


def create_project(slug='test', name='Test Project', status='o', public=True,
                    summary="SUMMARY", pitch="PITCH", tech="TECH", keywords=["KEYWORDS"],
                    proposal=ndb.Key('Proposal', 'test_proposal_key'),
                    category=ndb.Key('Category', 'test_category_key'),
                    creator=ndb.Key('User', 'test_user_key'),
                    ):
    return Project(key=ndb.Key('Project', slug), slug=slug, name=name, status=status, public=public,
                    summary=summary, pitch=pitch, tech=tech, keywords=keywords, proposal=proposal,
                    category=category, creator=creator
                    ).put()
