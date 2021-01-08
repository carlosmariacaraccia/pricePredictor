from json import JSONEncoder


class CattelDayPriceEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


class CattleDailyPrice:

    def __init__(self, *values):
        if len(values[0]) == 12:
            self.categoria = values[0][0]
            self.raza = values[0][1]
            self.cotas = values[0][2]
            self.precio_maximo = float(values[0][3].replace('$', '').replace(',', '.'))
            self.precio_minimo = float(values[0][4].replace('$', '').replace(',', '.'))
            self.precio_promedio = float(values[0][5].replace('$', '').replace(',', '.'))
            self.precio_mediana = float(values[0][6].replace('$', '').replace(',', '.'))
            self.cantidad_de_cabezas = float(values[0][7].replace('.', ''))
            self.peso_total_vendido = float(values[0][8].replace('.', '').replace(',', '.'))
            self.peso_promedio = float(values[0][9])
            self.importe_total_vendido = float(values[0][10].replace('.', '').replace(',', '.'))
            self.fecha = values[0][11]
        elif len(values[0]) == 10:
            self.categoria = values[0][0]
            self.raza = ''
            self.cotas = ''
            self.precio_maximo = float(values[0][1].replace('$', '').replace(',', '.'))
            self.precio_minimo = float(values[0][2].replace('$', '').replace(',', '.'))
            self.precio_promedio = float(values[0][3].replace('$', '').replace(',', '.'))
            self.precio_mediana = float(values[0][4].replace('$', '').replace(',', '.'))
            self.cantidad_de_cabezas = float(values[0][5].replace('.', ''))
            self.peso_total_vendido = float(values[0][6].replace('.', '').replace(',', '.'))
            self.peso_promedio = float(values[0][7])
            self.importe_total_vendido = float(values[0][8].replace('.', '').replace(',', '.'))
            self.fecha = values[0][9]
        elif len(values[0]) == 11:
            self.categoria = values[0][0]
            self.raza = values[0][1]
            self.cotas = ''
            self.precio_maximo = float(values[0][2].replace('$', '').replace(',', '.'))
            self.precio_minimo = float(values[0][3].replace('$', '').replace(',', '.'))
            self.precio_promedio = float(values[0][4].replace('$', '').replace(',', '.'))
            self.precio_mediana = float(values[0][5].replace('$', '').replace(',', '.'))
            self.cantidad_de_cabezas = float(values[0][6].replace('.', ''))
            self.peso_total_vendido = float(values[0][7].replace('.', '').replace(',', '.'))
            self.peso_promedio = float(values[0][8])
            self.importe_total_vendido = float(values[0][9].replace('.', '').replace(',', '.'))
            self.fecha = values[0][10]
