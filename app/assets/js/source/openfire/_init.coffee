## openfire object init
class Openfire

    constructor: (window) ->

        @sys =

            core_events: ['OPENFIRE_READY']

            state:
                status: 'NOT_READY' # System status
                flags: []           # System flags
                preinit: {}         # System preinit
                controllers: {}     # Installed system controllers
                classes: {}         # Installed openfire-related classes

                consider_preinit: (preinit) =>

                    # first consider classes
                    if preinit.abstract_base_classes?
                        for cls in preinit.abstract_base_classes
                            @sys.state.classes[cls.name] = cls
                            window[cls.name] = cls

                    # then controllers
                    if preinit.abstract_base_controllers?
                        for ctrlr in preinit.abstract_base_controllers

                            # save a reference
                            @sys.state.controllers[(c=ctrlr.name)] = ctrlr

                            # register controller events
                            window.apptools?.events?.register(event) for event in ctrlr.events

                            # instantiate & bind to window
                            window[c] = new ctrlr(@, window)

                            # last, init controller
                            window[c]._init?()

                    return preinit  # preinit HANDLED.

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
    window.$ = (id) -> window.Util?.get?(id) or document.getElementById(id)
    window.$.openfire = window.openfire