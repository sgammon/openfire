from apptools.services.builtin import Echo
from protorpc import messages, message_types, remote
from openfire.services import RemoteService


## Project
# Contains all project fields for users. Can be request or response.
class Project(messages.Message):
    slug = messages.StringField(1)
    name = messages.StringField(2)
    status = messages.StringField(3)
    category = messages.StringField(4)
    summary = messages.StringField(5)
    pitch = messages.StringField(6)
    tech = messages.StringField(7)
    keywords = messages.StringField(8)
    creator = messages.StringField(9)
    owners = messages.StringField(10, repeated=True)

    class Goal(messages.Message):
        contribution_type = messages.StringField(1)
        amount = messages.IntegerField(2)
        description = messages.StringField(3)
        backer_count = messages.IntegerField(4)
        progress = messages.StringField(5)
        met = messages.BooleanField(6)

    class Tier(messages.Message):
        amount = messages.IntegerField(1)
        description = messages.StringField(2)
        backer_count = messages.IntegerField(3)


## Projects
# A list of projects.
class Projects(messages.Message):
    projects = messages.MessageField(Project, 1, repeated=True)


## ProjectRequest
# Request project info or edit if project is populated.
class ProjectRequest(messages.Message):
    project_id = messages.StringField(1)
    project = messages.MessageField(Project, 2)


## Project service api.
#
class ProjectService(RemoteService):

    @remote.method(message_types.VoidMessage, Projects)
    def projects(self, request):

        ''' Returns a list of projects. '''

        return Projects()


    @remote.method(ProjectRequest, Project)
    def project(self, request):

        ''' Return, create, or edit a project. '''

        return Project()
