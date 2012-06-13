from apptools.services.builtin import Echo
from protorpc import message_types, remote
from openfire.services import RemoteService
from openfire.messages import proposal, common

class ProposalService(RemoteService):

    ''' Proposal service api. '''

    @remote.method(message_types.VoidMessage, proposal.Proposals)
    def list(self, request):

        ''' Returns a list of proposals. '''

        return proposal.Proposals()


    @remote.method(proposal.ProposalRequest, proposal.Proposal)
    def get(self, request):

        ''' Return, create, or edit a proposal. '''

        return proposal.Proposal()


    @remote.method(proposal.ProposalRequest, proposal.Proposal)
    def put(self, request):

        ''' Return, create, or edit a proposal. '''

        return proposal.Proposal()


    @remote.method(common.Comment, Echo)
    def comment(self, request):

        ''' Comment/iterate on a proposal. '''

        return Echo('You have commented on a proposal.')


    @remote.method(message_types.VoidMessage, common.Comments)
    def comments(self, request):

        ''' Comments for a proposal. '''

        return common.Comments()


    @remote.method(proposal.Promote, Echo)
    def promote(self, request):

        ''' Promote a proposal to become a project. '''

        return Echo('')


    @remote.method(proposal.SuspendProposal, Echo)
    def suspend(self, request):

        ''' Suspend a proposal. '''

        return Echo('')


    @remote.method(proposal.RejectProposal, Echo)
    def reject(self, request):

        ''' Reject a proposal. '''

        return Echo('')
