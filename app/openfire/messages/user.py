from protorpc import messages


class Profile(messages.Message):

    ''' Contains all profile fields for users. Can be request or response. '''

    username = messages.StringField(1)
    email = messages.StringField(2)
    firstname = messages.StringField(3)
    lastname = messages.StringField(4)
    bio = messages.StringField(5)


class ProfileRequest(messages.Message):

    ''' Request profile info or edit if profile is populated. '''

    user = messages.StringField(1)
    profile = messages.MessageField(Profile, 2)


class Account(messages.Message):

    ''' Contains all account info for users. Can be request or response. '''

    username = messages.StringField(1)
    email = messages.StringField(2)


class AccountRequest(messages.Message):

    ''' Request account info or edit if account is populated. '''

    user = messages.StringField(1)
    account = messages.MessageField(Account, 2)
