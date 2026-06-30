import webbrowser
from configs.settings import (
    YOUTUBE_URL,
    GITHUB_URL
)

def open_youtube():

    webbrowser.open(YOUTUBE_URL)

    
def open_github():

    webbrowser.open(GITHUB_URL)


def google_search(query):

    url = f"https://www.google.com/search?q={query}"

    webbrowser.open(url)
    
def open_google():

    webbrowser.open(
        "https://www.google.com"
    )

    return {

        "success": True
    }

def open_chatgpt():

    webbrowser.open(
        "https://chatgpt.com"
    )

    return {
        "success": True
    }