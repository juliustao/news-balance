import argparse

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def get_title(url):
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(urlopen(request), features="html.parser")
    return soup.title.string


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="", help="URL to get title of")
    args = parser.parse_args()

    url = args.url
    if not url:
        from url import get_current_url
        url = get_current_url()

    print("URL scraped:")
    print(url)

    title = get_title(url)
    print("\nTitle:")
    print(title)
