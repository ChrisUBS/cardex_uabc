# Librerías
import matplotlib.pyplot as plt
import pandas as pd
import json
from exportData.export_to_csv import get_ruta_carpeta

class GraficaBarras:

    def __init__(self, materia_seleccionada):
        self.materia_seleccionada = materia_seleccionada
        self.materia = self.obtener_materia()

    def generar_grafica(self):

        # Cargar el archivo CSV
        data = pd.read_csv(get_ruta_carpeta() + '/cardexUABC.csv')

        # Filtrar las calificaciones mayores de 60 de cada columna
        ord1 = data[data[self.materia + '_op1'] >= 60][self.materia + '_op1']
        extra1 = data[data[self.materia + '_op1_extra'] >= 60][self.materia + '_op1_extra']
        ord2 = data[data[self.materia + '_op2'] >= 60][self.materia + '_op2']
        extra2 = data[data[self.materia + '_op2_extra'] >= 60][self.materia + '_op2_extra']
        ord3 = data[data[self.materia + '_op3'] >= 60][self.materia + '_op3']
        extra3 = data[data[self.materia + '_op3_extra'] >= 60][self.materia + '_op3_extra']
        acre = data[data[self.materia + '_acre'] >= 60][self.materia + '_acre']
        reg = data[data[self.materia + '_reg'] >= 60][self.materia + '_reg']

        # Datos
        categorias = ['Ord 1', 'Extra 1', 'Ord 2', 'Extra 2', 'Ord 3', 'Extra 3', 'Acreditación', 'Regularización']
        valores = [ord1.count(), extra1.count(), ord2.count(), extra2.count(), ord3.count(), extra3.count(), acre.count(), reg.count()]

        # Crear el gráfico de barras
        plt.figure(num='Gráfica de barras', figsize=(12, 5))
        plt.bar(categorias, valores)

        # Añadir título y etiquetas
        plt.title(self.materia_seleccionada + " (Total estudiantes: " + str(len(data)) + ")")
        plt.xlabel("Oportunidades")
        plt.ylabel("Cantidad de aprobados")

        # Mostrar el gráfico
        plt.show()

    def obtener_materia(self):
        contenido_json = []

        with open('extractData\\subjects.json', 'r') as file:
            contenido_json = json.load(file)
        
        for materia in contenido_json:
            if contenido_json[materia][0] == self.materia_seleccionada:
                return materia