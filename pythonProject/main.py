import requests
from bs4 import BeautifulSoup
import time

class Currency:

    DOLLAR_RUB = 'https://www.google.com/search?q=exchange+rate+for+dollar&oq=exchange+rate+for+dollar&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTExNDQ0ajBqMagCALACAA&sourceid=chrome&ie=UTF-8'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

    current_converted_price = 0
    difference = 5

    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(",","."))

    def get_currency_price(self):

        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text
    def check_currency(self):
        currency = float(self.get_currency_price().replace(",","."))
        if currency >= self.current_converted_price + self.difference:
            print("exchange rate increased, do something!")
        if currency <= self.current_converted_price - self.difference:
            print("exchange rate decreased, do something")
        print("Now exchange rate is 1$ = ", str(currency))
        time.sleep(3)
        self.check_currency()


currency = Currency()
currency.check_currency()