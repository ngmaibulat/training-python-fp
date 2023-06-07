import requests


# url = "https://www.reddit.com/r/Python.rss"
url = "https://www.darkreading.com/rss.xml"


def fetch(url):
    response = requests.get(url)
    return response.text


# print(fetch(url))
