from configs.settings import (
    YOUTUBE_URL,
    GITHUB_URL
)

from modules.skills.open_url import (
    open_url
)


def open_google():

    return open_url(

        "https://www.google.com"

    )


def open_chatgpt():

    return open_url(

        "https://chatgpt.com"

    )


def open_youtube():

    return open_url(

        YOUTUBE_URL

    )


def open_github():

    return open_url(

        GITHUB_URL

    )


def google_search(
    query
):

    return open_url(

        f"https://www.google.com/search?q={query}"

    )