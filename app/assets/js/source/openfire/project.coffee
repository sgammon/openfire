## openfire project classes & controllers

# base project object
class Project extends OpenfireObject


# base proposal object
class Proposal extends OpenfireObject


# project controller
class ProjectController extends OpenfireController

    @events = []

    constructor: (openfire, window) ->
        return

    @_init: () =>
        return


# proposal controller
class ProposalController extends OpenfireController

    @events = []

    constructor: (openfire, window) ->
        return

    @_init: () =>
        return



@__openfire_preinit.abstract_base_objects.push(Project)
@__openfire_preinit.abstract_base_objects.push(Proposal)
@__openfire_preinit.abstract_base_controllers.push(ProjectController)
@__openfire_preinit.abstract_base_controllers.push(ProposalController)