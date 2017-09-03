from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, City, Category

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs


class Scrape:

    def __init__(self, country_id):
        self.country_id = country_id

    def run(self):
        months = ['01','02','03','04','05','06','07','08','09','10','11','12']
        categories = {'avg_temperature_high': 'TX', 'avg_temperature_low': 'TN',
                      'avg_rain_mass': 'NS', 'rain_days': 'ND', 'strong_wind_days': 'FXD',
                      'wind_speed': 'FFkmh', 'frost_days': 'FD'}
        countries_ids = {'berlin': 10382, 'moscow': 27612}

        for country in countries_ids:
            print(country)
            for category in categories:
                for month in months:
                    url = 'http://www.wetteronline.de/?pcid=pc_rueckblick_climate&gid=' \
                          + str(countries_ids[country]) \
                          + '&iid=' \
                          + str(countries_ids[country]) \
                          + '&pid=p_rueckblick_climatecalculator&sid=Default&var=' \
                          + categories[category] \
                          + '&analysis=monthly&month=' \
                          + month \
                          + '&startyear=1990&endyear=2017&iid=10382'
                    req = Request(url,
                                  headers={'User-Agent': 'Mozilla/5.0'})
                    webpage = urlopen(req).read()
                    webpage = webpage.decode('utf-8')
                    soup = bs(webpage, 'html.parser')
                    table = soup.tbody
                    print('\nCategory         Month\n' + category + ' ' + month + '\n')
                    for row in table.findAll('tr'):
                        counter = 0
                        for td in row.find_all('td'):
                            if counter % 2 is 0:
                                print('Year ', td.get_text())
                            else:
                                print('Value ', td.get_text())
                            counter += 1


s = Scrape(10382)
s.run()
