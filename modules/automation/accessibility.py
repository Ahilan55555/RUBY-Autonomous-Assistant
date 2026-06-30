import pyatspi


def get_desktop():

    return pyatspi.Registry.getDesktop(0)

def list_applications():

    desktop = get_desktop()

    apps = []

    for app in desktop:

        if app:

            apps.append(
                app.name
            )

    return apps

def list_children(accessible):

    children = []

    for child in accessible:

        if child:

            children.append(child)

    return children


def find_application(name):

    desktop = get_desktop()

    name = name.lower()

    for app in desktop:

        if app and name in app.name.lower():

            return app

    return None

def print_tree(
    node,
    depth=0
):

    if node is None:
        return

    indent = "    " * depth

    try:
        print(
            f"{indent}{node.name} | {node.getRoleName()}"
        )
    except Exception:
        pass

    try:
        for child in node:
            print_tree(
                child,
                depth + 1
            )
    except Exception:
        pass


def get_ui_elements(
    node,
    elements=None
):

    if elements is None:
        elements = []

    if node is None:
        return elements

    try:

        # ---------- States ----------

        try:

            state_set = node.getState()

            states = [
                str(state)
                for state in state_set.getStates()
            ]

        except Exception:

            states = []

        # ---------- Bounds ----------

        try:

            component = node.queryComponent()

            rect = component.getExtents(
                pyatspi.XY_SCREEN
            )

            bounds = {
                "x": rect.x,
                "y": rect.y,
                "width": rect.width,
                "height": rect.height
            }

        except Exception:

            bounds = None

        # ---------- Store Element ----------

        elements.append(
            {
                "node": node,
                "name": node.name,
                "role": node.getRoleName(),
                "states": states,
                "bounds": bounds
            }
        )

    except Exception:
        pass

    try:

        for child in node:

            get_ui_elements(
                child,
                elements
            )

    except Exception:
        pass

    return elements


def find_elements_by_role(
    elements,
    role
):

    return [

        element

        for element in elements

        if element["role"] == role

    ]


def find_elements_by_name(
    elements,
    text
):

    text = text.lower()

    return [

        element

        for element in elements

        if text in element["name"].lower()

    ]


def find_first_role(
    elements,
    role
):

    for element in elements:

        if element["role"] == role:

            return element

    return None


def find_first_name(
    elements,
    text
):

    text = text.lower()

    for element in elements:

        if text in element["name"].lower():

            return element

    return None

def find_all_role(
    elements,
    role
):

    matches = []

    for element in elements:

        if element["role"] == role:

            matches.append(element)

    return matches


def find_by_role(
    application_name,
    role
):

    app = find_application(
        application_name
    )

    if app is None:
        return []

    elements = get_ui_elements(
        app
    )

    return [

        element

        for element in elements

        if element["role"] == role

    ]


def find_first_editable_entry(
    application_name
):

    entries = find_by_role(
        application_name,
        "entry"
    )

    for entry in entries:

        states = " ".join(
            entry["states"]
        ).lower()

        if (
            "editable" in states
            and
            "enabled" in states
            and
            "visible" in states
            and
            "showing" in states
        ):

            return entry

    return None


def find_all_buttons(
    application_name
):

    return find_by_role(
        application_name,
        "push button"
    )


def find_all_links(
    application_name
):

    return find_by_role(
        application_name,
        "link"
    )


def find_by_name(
    application_name,
    text
):

    app = find_application(
        application_name
    )

    if app is None:
        return []

    elements = get_ui_elements(app)

    return find_elements_by_name(
        elements,
        text
    )