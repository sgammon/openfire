from protorpc import messages
from openfire.messages.common import Goal, Tier


class Proposal(messages.Message):

    ''' Contains all proposal fields for users. Can be request or response. '''

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
    goals = messages.MessageField(Goal, 11, repeated=True)
    tiers = messages.MessageField(Tier, 12, repeated=True)


class Proposals(messages.Message):

    ''' A list of proposals. '''

    proposals = messages.MessageField(Proposal, 1, repeated=True)


class ProposalRequest(messages.Message):

    ''' Request proposal info, or, if proposal is populated, edit profile. '''

    proposal_id = messages.StringField(1)
    proposal = messages.MessageField(Proposal, 2)
    is_new = messages.BooleanField(3, default=False)


class Promote(messages.Message):

    ''' Request proposal info, or, if proposal is populated, edit profile. '''

    proposal_id = messages.StringField(1)


class RejectProposal(messages.Message):

    ''' Reject a proposal. '''

    proposal_id = messages.StringField(1)
    reason = messages.StringField(2)


class SuspendProposal(messages.Message):

    ''' Suspend a proposal. '''

    proposal_id = messages.StringField(1)
    reason = messages.StringField(2)
