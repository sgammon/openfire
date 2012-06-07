from apptools.services.builtin import Echo
from protorpc import messages, message_types, remote
from openfire.services import RemoteService


## Proposal
# Contains all proposal fields for users. Can be request or response.
class Proposal(messages.Message):
    slug = messages.StringField(1)
    name = messages.StringField(2)
    status = messages.StringField(3)
    category = messages.StringField(4)
    summary = messages.StringField(5)
    pitch = messages.IntegerField(6)
    tech = messages.StringField(7)
    keywords = messages.StringField(8)
    creator = messages.StringField(9)
    owners = messages.StringField(10, repeated=True)


## Proposals
# A list of proposals.
class Proposals(messages.Message):
    proposals = messages.MessageField(Proposal, 1, repeated=True)


## ProposalRequest
# Request proposal info or edit if proposal is populated.
class ProposalRequest(messages.Message):
    proposal_id = messages.StringField(1)
    proposal = messages.MessageField(Proposal, 2)
    is_new = messages.BooleanField(3, default=False)


## ProposalComment
# Comment on a proposal as an owner or a site admin.
class ProposalComment(messages.Message):
    proposal_id = messages.StringField(1)
    text = messages.StringField(2)


## ProposalComments
# A list of proposal comments for a proposal.
class ProposalComments(messages.Message):
    comments = messages.MessageField(ProposalComment, 1, repeated=True)


## Proposal service api.
#
class ProposalService(RemoteService):

    @remote.method(message_types.VoidMessage, Proposals)
    def proposals(self, request):

        ''' Returns a list of proposals. '''

        return Proposals()


    @remote.method(ProposalRequest, Proposal)
    def proposal(self, request):

        ''' Return, create, or edit a proposal. '''

        return Proposal()


    @remote.method(ProposalComment, Echo)
    def comment(self, request):

        ''' Comment/iterate on a proposal. '''

        return Echo("You have commented on a proposal.")


    @remote.method(ProposalRequest, ProposalComments)
    def comments(self, request):

        ''' Return a list of comments on this proposal. '''

        return ProposalComments()
