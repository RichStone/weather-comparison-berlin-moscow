from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

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
                for td in row.find_all('td'):
                    print(td.get_text())
