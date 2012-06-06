from apptools.services.builtin import Echo
from protorpc import messages, message_types, remote
from project.services import RemoteService


## Profile
# Contains all profile fields for users. Can be request or response.
class Profile(messages.Message):
    username = messages.StringField(1)
    email = messages.StringField(2)
    firstname = messages.StringField(3)
    lastname = messages.StringField(4)
    bio = messages.StringField(5)


## ProfileRequest
# Request profile info or edit if profile is populated.
class ProfileRequest(messages.Message):
    user = messages.StringField(1)
    profile = messages.MessageField(Profile, 2)


## Account
# Contains all account info for users. Can be request or response.
class Account(messages.Message):
    username = messages.StringField(1)
    email = messages.StringField(2)


## AccountRequest
# Request account info or edit if account is populated.
class AccountRequest(messages.Message):
    user = messages.StringField(1)
    account = messages.MessageField(Account, 2)


## FollowRequest
# Request to follow a user.
class FollowRequest(messages.Message):
    user = messages.StringField(1)


## FollowersResponse
# Request to see the followers of a user
class FollowersRequest(messages.Message):
    user = messages.StringField(1)


## FollowersResponse
# Response containing a list of followers.
class FollowersResponse(messages.Message):
    profiles = messages.MessageField(Profile, 1, repeated=True)


## User service api.
#
class UserService(RemoteService):

    @remote.method(ProfileRequest, Profile)
    def profile(self, request):

        ''' Return or edit profile information for a user '''

        return Profile()


    @remote.method(AccountRequest, Account)
    def account(self, request):

        ''' Return or edit account information for a user. '''

        return Account()


    @remote.method(FollowRequest, Echo)
    def follow(self, request):

        ''' Return following success or failure message. '''

        return Echo(message="You are now following someone...or not.")


    @remote.method(FollowersRequest, FollowersResponse)
    def followers(self, request):

        ''' Return the followers of a user. Returns a list of user profiles. '''

        return FollowersResponse()
