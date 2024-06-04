# Librerías
import matplotlib.pyplot as plt
import pandas as pd
import json
from exportData.export_to_csv import get_ruta_carpeta

class GraficaArea:

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
        categorias = ['Ord 1', 'Extra 1', 'Ord 2', 'Extra 2', 'Ord 3', 'Extra 3']
        promedio = [ord1.mean(), extra1.mean(), ord2.mean(), extra2.mean(), ord3.mean(), extra3.mean()]

        # Crear el gráfico de área
        plt.figure(num='Gráfica de área')
        plt.fill_between(categorias, promedio)
        plt.plot(categorias, promedio, color="red", alpha=0.6)

        # Añadir título y etiquetas
        plt.title(self.materia_seleccionada + " (Promedios)")
        plt.xlabel('Oportunidades')
        plt.ylabel('Calificación promedio')

        # Añadir nombres en el eje x
        plt.xticks(categorias)

        # Mostrar el gráfico
        plt.show()

    def obtener_materia(self):
        contenido_json = []

        with open('extractData\\subjects.json', 'r') as file:
            contenido_json = json.load(file)
        
        for materia in contenido_json:
            if contenido_json[materia][0] == self.materia_seleccionada:
                return materia