capabilities = {}


def register_capability(

    intent,

    target=None
):
    
    if intent not in capabilities:

        capabilities[intent] = []


    if target is not None:

        capabilities[intent].append(

            target
        )

    else:

        capabilities[intent] = True


def has_capability(

    intent,

    target=None
):

    if intent not in capabilities:

        return False


    capability = capabilities[intent]


    if capability is True:

        return True


    if target is None:

        return False


    return target in capability


def show_capabilities():

    return capabilities