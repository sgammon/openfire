from protorpc import messages

class AddMedia(messages.Message):

    ''' Add media. '''

    media = messages.StringField(1)


class Media(messages.Message):

    ''' Get media. '''

    media = messages.StringField(1)
