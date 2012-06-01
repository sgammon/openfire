## openfire core classes

# setup preinit container (picked up in openfire init)
if @__openfire_preinit?
    @__openfire_preinit.abstract_base_controllers = []
    @__openfire_preinit.abstract_base_classes = []
else
    @__openfire_preinit =
        abstract_base_controllers: []   # base controllers setup before init
        abstract_base_classes: []       # base classes setup before init

# openfire controller: base controller class for frontend services
class OpenfireController
@__openfire_preinit.abstract_base_controllers.push OpenfireController

# openfire exception: base error for openfire-level errors
class OpenfireException extends Error

    constructor: (@controller, @message, @context) ->
    toString: () ->
        return '[' + @controller + '] OpenfireException: ' + @message

@__openfire_preinit.abstract_base_classes.push OpenfireException