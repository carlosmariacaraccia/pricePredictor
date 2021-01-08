from CattleDailyPrice import *
from bs4 import BeautifulSoup
from datetime import date


class ParseMercadoDeLiniersWebPage:

    # function to parse the 'resumen analitico de precios'
    # we will obtain an array of data to feed an ml algorithm
    @staticmethod
    def parse_resumen_analitico_de_precios(html_source: str, parsing_date: date):

        # load the Beatiful Soup parser
        soup = BeautifulSoup(html_source, features='html.parser')
        soup = soup.find('table', attrs={'class': 'clsTextoCarteleraChico'})
        # get all the table rows
        rows = soup.find_all('tr')

        # store the returning data
        data_per_day = []

        for row in rows:
            # find the table data
            columns = row.find_all('td')
            # get the string values of the extracted elements
            columns = [ele.text.strip() for ele in columns]
            # add the iteration date
            columns.append(parsing_date)
            # remove the empty elements
            purged_data = [ele for ele in columns if ele]
            # append only the necessary elements
            if (len(purged_data) != 1) and ('Totales' not in purged_data):
                data_per_day.append(purged_data)

        # now we will remove the null elements
        data_per_day = [x for x in data_per_day if len(x) != 0]

        # convert the data per day into an array of custom objects
        cattle_prices_per_day = list(map(CattleDailyPrice, data_per_day))
        if len(cattle_prices_per_day) != 0:
            cattle_prices_day_dict = [cattle_day_price.__dict__ for cattle_day_price in cattle_prices_per_day]
            cattle_prices_per_day_list = (list([list(cattle_price_day.values()) for cattle_price_day in cattle_prices_day_dict]))
            return cattle_prices_per_day_list
