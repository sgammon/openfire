from apptools.services.builtin import Echo
from protorpc import message_types, remote
from openfire.services import RemoteService
from openfire.messages import auth


class AuthService(RemoteService):

    ''' Auth service api. '''

    @remote.method(auth.Login, auth.Login)
    def login(self, request):

        ''' User log in. '''

        return auth.Login()


    @remote.method(message_types.VoidMessage, Echo)
    def logout(self, request):

        ''' User log out. '''

        return Echo('You have logged out.')


    @remote.method(message_types.VoidMessage, auth.Session)
    def session(self, request):

        ''' Get a user session. '''

        return auth.Session()


    @remote.method(auth.Request, auth.Request)
    def request(self, request):

        ''' Request '''

        return auth.Request()


    @remote.method(auth.Verify, Echo)
    def verify(self, request):

        ''' Verify a user email or permission. '''

        return Echo('')


    @remote.method(auth.ThirdParty, Echo)
    def thirdparty(self, request):

        ''' Authenticate against a third party auth provider. '''

        return Echo('')


    @remote.method(message_types.VoidMessage, auth.Session)
    def renew(self, request):

        ''' Renew a user session. '''

        return auth.Session()


    @remote.method(auth.SignUp, Echo)
    def signup(self, request):

        ''' Sign up a new user. '''

        return Echo('')
