from MLWebPageNavigator import *
from Scrapper import *
from datetime import date
from datetime import timedelta
from turicreate import SFrameBuilder


class MercadoDeLiniersPricesSummary:

    @staticmethod
    def data_sframe_for_dates(initial_date: date, ending_date: date, path_to_save: str):

        # get the driver of the web page
        driver = MercadoDeLiniersNavigator.go_to_initial_resumen_de_precios()

        # initialize the sframe with column types and column names
        colunm_types = [str, str, str, float, float, float, float, float, float, float, float, date]
        column_names = ['categoria', 'raza', 'cotas', 'precio_maximo', 'precio_minimo', 'precio_promedio',
                        'precio_mediana', 'cantidad_de_cabezas', 'peso_total_vendido', 'peso_promedio',
                        'importe_total_vendido', 'fecha']

        sframe_to_be_built = SFrameBuilder(column_types=colunm_types, column_names=column_names)

        while initial_date <= ending_date:
            source = MercadoDeLiniersNavigator.get_cattle_prices_for_a_date(driver=driver,
                                                                            date_to_pick=initial_date)
            resulting_list = ParseMercadoDeLiniersWebPage.parse_resumen_analitico_de_precios(html_source=source,
                                                                                             parsing_date=initial_date)
            initial_date += timedelta(days=1)
            if resulting_list is not None:
                sframe_to_be_built.append_multiple(resulting_list)

        # once the loop has finished close the sframe and save it to a path
        resulting_sframe = sframe_to_be_built.close()
        return resulting_sframe
