import requests


class NewsFeed:
    """ representing multiple news title and links as a single string """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "74818f55dedf4a6eaee8d4893a3100a0"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)
        
        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


news_feed = NewsFeed(interest="nasa", from_date="2022-09-01", to_date="2022-09-02", language="en")
print(news_feed.get())