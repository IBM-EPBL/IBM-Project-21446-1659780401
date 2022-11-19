import json

import requests


def get_news(source):
    url = "https://newsapi.org/v1/articles?apiKey=1d786ef6f8b54b8b88748b8b639d6a19&source={}".format(source)
    news_data = requests.get(url).json()
    news = []

    for article in news_data["articles"]:
        news.append({
            "author": article["author"],
            'title': article["title"],
            'desc': article["description"],
            'url': article["url"],
            'img': article['urlToImage']
        })

    return news


# def news_return(source):
#     # with open("sources.json") as sources:
#     #     sources = json.load(sources)
#     #     for source in sources:
#     #         print("{}. {}".format(source["num"], source["name"]))
#     #
#     #     source_num = int(input("Choose source: "))
#
#     data = get_news("reuters")
#
#     return data


class news_article(object):
    def __init__(self, author, title, desc, url, img):
        self.author = author
        self.title = title
        self.desc = desc
        self.url = url
        self.img = img

    def print_article(self):
        print(self.author)
        print(self.title)
        print(self.desc)


def main(source):
    news_data = get_news(source)

    articles = []
    for article in news_data:
        single_news_article = news_article(article["author"], article["title"], article["desc"], article["url"],
                                           article["img"])
        articles.append(single_news_article)

    return articles


