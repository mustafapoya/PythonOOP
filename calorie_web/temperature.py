from selectorlib import Extractor
import requests


class Temperature:
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9,fa-AF;q=0.8,fa;q=0.7',
    }

    base_url = "https://www.timeanddate.com/weather/"
    yml_path = "temperature.yaml"

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        url = self.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers=self.headers)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace("\xa0°C", ""))


if __name__ == "__main__":
    temperature = Temperature(country="usa", city="san francisco")
    print(temperature.get())

