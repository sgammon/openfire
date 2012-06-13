from apptools.services.builtin import Echo
from protorpc import message_types, remote
from openfire.services import RemoteService
from openfire.messages import project, common, media


class ProjectService(RemoteService):

    ''' Project service api. '''

    @remote.method(message_types.VoidMessage, project.Projects)
    def list(self, request):

        ''' Returns a list of projects. '''

        return project.Projects()


    @remote.method(project.ProjectRequest, project.Project)
    def get(self, request):

        ''' Return a project. '''

        return project.Project()


    @remote.method(project.ProjectRequest, project.Project)
    def put(self, request):

        ''' Create or edit a project. '''

        return project.Project()


    @remote.method(common.Comment, Echo)
    def comment(self, request):

        ''' Comment on a project. '''

        return Echo('')


    @remote.method(common.Comments, Echo)
    def comments(self, request):

        ''' Return comments for a project. '''

        return common.Comments()


    @remote.method(common.Post, Echo)
    def post(self, request):

        ''' Post and update to a project. '''

        return Echo


    @remote.method(message_types.VoidMessage, common.Posts)
    def posts(self, request):

        ''' Return posts for a project. '''

        return common.posts()


    @remote.method(media.AddMedia, media.Media)
    def add_media(self, request):

        ''' Add media to a project. '''

        return media.Media()


    @remote.method(message_types.VoidMessage, media.Media)
    def media(self, request):

        ''' Return media for a project. '''

        return common.Media()


    @remote.method(common.FollowRequest, Echo)
    def follow(self, request):

        ''' Follow a project. '''

        return Echo('')


    @remote.method(common.FollowersRequest, common.FollowersResponse)
    def followers(self, request):

        ''' Return followers of a project. '''

        return common.FollowersResponse()


    @remote.method(message_types.VoidMessage, project.Backers)
    def backers(self, request):

        ''' Return backers of a project. '''

        return project.Backers()


    @remote.method(project.BackProject, Echo)
    def back(self, request):

        ''' Become a backer of a project. '''

        return Echo('')


    @remote.method(project.SuspendProject, Echo)
    def suspend(self, request):

        ''' Suspend a project. '''

        return Echo('')


    @remote.method(project.ShutdownProject, Echo)
    def shutdown(self, request):

        ''' Shut down a project. '''

        return Echo('')
