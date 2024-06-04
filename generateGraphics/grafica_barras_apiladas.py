# Librerías
import matplotlib.pyplot as plt
import pandas as pd
import json
from exportData.export_to_csv import get_ruta_carpeta

class GraficaBarrasApiladas:

    def __init__(self, materia_seleccionada):
        self.materia_seleccionada = materia_seleccionada
        self.materia = self.obtener_materia()

    def generar_grafica(self):

        # Cargar el archivo CSV
        data = pd.read_csv(get_ruta_carpeta() + '/cardexUABC.csv')

        # Extraer las calificaciones de la materia seleccionada
        ord1 = data[data[self.materia + '_op1'] >= 0][self.materia + '_op1']
        extra1 = data[data[self.materia + '_op1_extra'] >= 0][self.materia + '_op1_extra']
        ord2 = data[data[self.materia + '_op2'] >= 0][self.materia + '_op2']
        extra2 = data[data[self.materia + '_op2_extra'] >= 0][self.materia + '_op2_extra']
        ord3 = data[data[self.materia + '_op3'] >= 0][self.materia + '_op3']
        extra3 = data[data[self.materia + '_op3_extra'] >= 0][self.materia + '_op3_extra']

        # Datos
        categorias = ['1', '2', '3']
        valores1 = [ord1.count(), ord2.count(), ord3.count()]
        valores2 = [extra1.count(), extra2.count(), extra3.count()]

        # Crear el gráfico de barras apiladas
        plt.figure(num='Gráfica de barras apiladas')
        plt.bar(categorias, valores1, label='Ordinarios')
        plt.bar(categorias, valores2, bottom=valores1, label='Extras')

        # Añadir título y etiquetas
        plt.title(self.materia_seleccionada + " (Cantidades de ordis y extras)")
        plt.xlabel('Oportunidad')
        plt.ylabel('Cantidad')

        # Mostrar el gráfico
        plt.legend()
        plt.show()

    def obtener_materia(self):
        contenido_json = []

        with open('extractData\\subjects.json', 'r') as file:
            contenido_json = json.load(file)
        
        for materia in contenido_json:
            if contenido_json[materia][0] == self.materia_seleccionada:
                return materia