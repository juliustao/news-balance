from urllib.parse import quote

from requests_html import HTMLSession


def get_url_to_scrape(article_title):
    # Given an article title, get the AllSides.com URL to scrape centrist articles
    # Example title:
    # New Year, new laws: Obamacare, pot, guns and drones
    url_to_scrape = "https://www.allsides.com/allsides-search-results"
    url_to_scrape += "?search_api_views_fulltext="
    query = quote(article_title, safe='')
    query_with_plus = query.replace("%20", "+")
    url_to_scrape += query_with_plus
    url_to_scrape += "&search="
    url_to_scrape += query_with_plus
    url_to_scrape += "&created=2&submit.x=0&submit.y=0#gsc.tab=0&gsc.q="
    url_to_scrape += query
    url_to_scrape += "&gsc.sort=&gsc.ref=more%3Acenter&gsc.page=1"
    return url_to_scrape


def scrape_url(url_to_scrape, n=5):
    # Scrape the given AllSides.com URL for the first article
    session = HTMLSession()
    r = session.get(url_to_scrape)
    r.html.render()
    result = r.html.find("[data-ctorig]", first=True)
    url = result.attrs["data-ctorig"]
    return url