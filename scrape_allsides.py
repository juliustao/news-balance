import argparse
from urllib.request import Request, urlopen
from urllib.parse import quote

from bs4 import BeautifulSoup


def get_allsides_url(title):
    # example title:
    # New Year, new laws: Obamacare, pot, guns and drones
    allsides_url = "https://www.allsides.com/allsides-search-results"
    allsides_url += "?search_api_views_fulltext="
    query = quote(title, safe='')
    query_with_plus = query.replace("%20", "+")
    allsides_url += query_with_plus
    allsides_url += "&search="
    allsides_url += query_with_plus
    allsides_url += "&created=2&submit.x=0&submit.y=0#gsc.tab=0&gsc.q="
    allsides_url += query
    allsides_url += "&gsc.sort=&gsc.ref=more%3Acenter"
    return allsides_url


if __name__ == "__main__":
    from title import get_title
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

    allsides_url = get_allsides_url(title)
    print("\nAllSides URL:")
    print(allsides_url)
