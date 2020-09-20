from newspaper import Article


def get_title(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.title
