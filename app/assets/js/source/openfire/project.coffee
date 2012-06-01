## openfire project controllers
class ProjectController extends OpenfireController

    @events = []

    constructor: (openfire, window) ->
        return

    @_init: () =>
        return

class ProposalController extends OpenfireController

    @events = []

    constructor: (openfire, window) ->
        return

    @_init: () =>
        return

@__openfire_preinit.abstract_base_controllers.push(ProjectController)