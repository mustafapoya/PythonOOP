import requests, pprint


class Weather:
    """
    Create a weather object getting an api key as input, and either a city name or lat and lon coordinates.
    """
    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments")

        if self.data['code'] != "200":
            raise ValueError(self.data['message'])

    def next_12h(self):
        """
        get next 12 hour
        """
        return self.data['list'][0:4]

    def next_12h_simplified(self):
        """
        get next 12 hour simplified
        """
        sample_data = []
        for dicty in self.data["list"][:4]:
            sample_data.append((dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description']))

        return sample_data


# weather = Weather(apikey="7d61a27fd086efac30150748186932a5", city="Valencia")
# pprint.pprint(weather.data)
# pprint.pprint(weather.next_12h_simplified())