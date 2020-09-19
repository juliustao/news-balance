import argparse
from newspaper import Article


def get_title(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.title


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
