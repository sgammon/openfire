## openfire core classes

# setup preinit container (picked up in openfire init)
if @__openfire_preinit?
    @__openfire_preinit.abstract_base_objects = []
    @__openfire_preinit.abstract_base_classes = []
    @__openfire_preinit.abstract_base_controllers = []
else
    @__openfire_preinit =
        abstract_base_objects: []       # objects to preinit
        abstract_base_classes: []       # classes to preinit
        abstract_base_controllers: []   # controllers to preinit


# openfire object: base object
class OpenfireObject extends CoreObject


# openfire controller: base controller class for frontend services
class OpenfireController


# openfire exception: base error for openfire-level errors
class OpenfireException extends Error

    constructor: (@controller, @message, @context) ->
    toString: () ->
        return '[' + @controller + '] OpenfireException: ' + @message



@__openfire_preinit.abstract_base_objects.push OpenfireObject
@__openfire_preinit.abstract_base_controllers.push OpenfireController
@__openfire_preinit.abstract_base_classes.push OpenfireException