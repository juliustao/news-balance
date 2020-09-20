import argparse

from scrape import get_url_to_scrape, scrape_url
from title import get_title


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="", help="URL of partisan article")
    args = parser.parse_args()

    current_url = args.url
    print("URL scraped:")
    print(current_url)

    article_title = get_title(current_url)
    print("\nTitle:")
    print(article_title)

    url_to_scrape = get_url_to_scrape(article_title)
    print("\nAllSides URL:")
    print(url_to_scrape)

    centrist_url = scrape_url(url_to_scrape)
    print("\nCentrist URL:")
    print(centrist_url)
