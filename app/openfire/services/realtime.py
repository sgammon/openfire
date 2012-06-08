from apptools.services.builtin import Echo
from protorpc import message_types, remote
from openfire.services import RemoteService


class RealtimeService(RemoteService):

    ''' Realtime service api. '''

    @remote.method(message_types.VoidMessage, Echo)
    def establish(self, request):

        ''' Establish a realtime connection. '''

        return Echo('Established!')


    @remote.method(message_types.VoidMessage, Echo)
    def renew(self, request):

        ''' Renew a realtime connection. '''

        return Echo('Renewed')


    @remote.method(message_types.VoidMessage, Echo)
    def ping(self, request):

        ''' Ping. '''

        return Echo('Ping')


    @remote.method(message_types.VoidMessage, Echo)
    def manifest(self, request):

        ''' Manifest. '''

        return Echo('Manifest')
