import webbrowser


def open_url(
    url
):

    try:

        webbrowser.open(
            url
        )

        return {

            "success": True,

            "url": url

        }

    except Exception as error:

        return {

            "success": False,

            "error": str(error)

        }