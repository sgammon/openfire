## openfire page init
class Openfire

    constructor: (window) ->

        @sys =

            core_events: ['OPENFIRE_READY']

            # internal state
            state:

                status: 'NOT_READY' # System status
                flags: []           # System flags
                preinit: {}         # System preinit
                controllers: {}     # Installed system controllers
                classes: {}         # Installed openfire-related classes
                objects: {}         # Installed openfire-related objects

                consider_preinit: (preinit) =>

                    # first consider base objects
                    if preinit.abstract_base_objects?
                        @sys.install.object(obj) for obj in preinit.abstract_base_objects?

                    # next classes
                    if preinit.abstract_base_classes?
                        @sys.install.class(cls) for cls in preinit.abstract_base_classes

                    # then controllers
                    if preinit.abstract_base_controllers?
                        @sys.install.controller(ctrlr) for ctrlr in preinit.abstract_base_controllers

                    return preinit  # preinit HANDLED.

            install:
                # installs an openfire base object
                object: (obj) =>
                    # stash for future queries
                    @sys.state.objects[(o=obj.constructor.name)] = obj

                    # register any object events
                    if obj.events?
                        window.apptools?.events?.register(event) for event in obj.events

                    # instantiate and bind to window, if obj isn't private
                    if obj.export? isnt 'private' then window[o] = obj = new obj(@) else obj = new obj()

                    # lastly init, if it needs it
                    obj._init?()

                    return obj

                # installs an openfire base class
                class: (cls) =>
                    @sys.state.classes[(cl=cls.constructor.name)] = cls
                    if cls.events?
                        window.apptools?.events?.register(event) for event in cls.events
                    if cls.export? isnt 'private' then window[cl] = cls = new cls(@) else cls = new cls()
                    cls._init?()

                    return cls

                # installs an openfire controller
                controller: (ctrlr) =>
                    @sys.state.controllers[(c=ctrlr.constructor.name)] = ctrlr
                    if ctrlr.events?
                        window.apptools?.events?.register(event) for event in ctrlr.events
                    if ctrlr.export? isnt 'private' then window[c] = ctrlr = new ctrlr(@, window) else ctrlr = new ctrlr(@, window)
                    ctrlr._init?()

                    return ctrlr


            go: () =>
                # oh snap it's go time
                window.apptools?.dev?.verbose 'Openfire', 'Openfire systems go.'
                @sys.state.status = 'READY'
                return @

        # consider preinit
        if window.__openfire_preinit?
            @sys.state.preinit = window.__openfire_preinit
            @sys.state.consider_preinit(window.__openfire_preinit)

        ### Init code will go here, if we actually need any more. ###

        # trigger system ready
        return @sys.go()

# bind openfire to window
window.Openfire = Openfire
window.openfire = new Openfire()

# if jQuery's around, extend it with openfire
if $?
    $.extend openfire: window.openfire

# otherwise, we got this on lock.
else

    window.$ = (id) -> if window.Util? then window.Util.get(id) else document.getElementById(id)
    window.$.openfire = window.openfire