from protorpc import messages

class Goal(messages.Message):

    ''' Common to proposals and projects, defines a funding goal. '''

    contribution_type = messages.StringField(1)
    amount = messages.IntegerField(2)
    description = messages.StringField(3)
    backer_count = messages.IntegerField(4)
    progress = messages.StringField(5)
    met = messages.BooleanField(6)


class Tier(messages.Message):

    ''' Common to proposals and projects, defines a contribution tier. '''

    amount = messages.IntegerField(1)
    description = messages.StringField(2)
    backer_count = messages.IntegerField(3)


class Comment(messages.Message):

    ''' Comment on something. '''

    username = messages.StringField(1)
    text = messages.StringField(2)


class Comments(messages.Message):

    ''' A list of comments. '''

    comments= messages.MessageField(Comment, 1, repeated=True)


class Post(messages.Message):

    ''' Post something. '''

    username = messages.StringField(1)
    text = messages.StringField(2)


class Posts(messages.Message):

    ''' A list of posts. '''

    posts = messages.MessageField(Post, 1, repeated=True)


class FollowRequest(messages.Message):

    ''' Request to follow a user. '''

    user = messages.StringField(1)


class FollowersRequest(messages.Message):

    ''' Request to see the followers of a user '''

    user = messages.StringField(1)


class FollowersResponse(messages.Message):

    ''' Response containing a list of follower usernames. '''

    profiles = messages.StringField(1, repeated=True)
