# Librerías
import matplotlib.pyplot as plt
import pandas as pd
import json
from exportData.export_to_csv import get_ruta_carpeta

class GraficaPastel:

    def __init__(self, materia_seleccionada):
        self.materia_seleccionada = materia_seleccionada
        self.materia = self.obtener_materia()

    def generar_grafica(self):

        # Cargar el archivo CSV
        data = pd.read_csv(get_ruta_carpeta() + '/cardexUABC.csv')

        # Filtrar las calificaciones mayores de 60 de cada columna
        ord1 = data[data[self.materia + '_op1'] >= 60][self.materia + '_op1']
        ord2 = data[data[self.materia + '_op2'] >= 60][self.materia + '_op2']
        ord3 = data[data[self.materia + '_op3'] >= 60][self.materia + '_op3']
        extra1 = data[data[self.materia + '_op1_extra'] >= 60][self.materia + '_op1_extra']
        extra2 = data[data[self.materia + '_op2_extra'] >= 60][self.materia + '_op2_extra']
        extra3 = data[data[self.materia + '_op3_extra'] >= 60][self.materia + '_op3_extra']
        acre = data[data[self.materia + '_acre'] >= 60][self.materia + '_acre']
        reg = data[data[self.materia + '_reg'] >= 60][self.materia + '_reg']

        # Sumar la cantidad de aprobados
        aprobados_ordi = ord1.count() + ord2.count() + ord3.count()
        aprobados_extra = extra1.count() + extra2.count() + extra3.count()
        aprobados_otros = acre.count() + reg.count()

        # Datos
        categorias = []
        porcentajes = []
        if aprobados_ordi > 0:
            categorias.append('Ordis')
            porcentajes.append(aprobados_ordi)
        if aprobados_extra > 0:
            categorias.append('Extras')
            porcentajes.append(aprobados_extra)
        if aprobados_otros > 0:
            categorias.append('Otros')
            porcentajes.append(aprobados_otros)

        # Crear el gráfico de pastel
        plt.figure(num='Gráfica pastel')
        plt.pie(porcentajes, labels=categorias, autopct='%1.1f%%', startangle=140)

        # Añadir título
        plt.title(self.materia_seleccionada + " (Aprobados por cada categoría)")

        # Mostrar el gráfico
        plt.axis('equal')  # Asegurar que el gráfico de pastel sea un círculo
        plt.show()

    def obtener_materia(self):
        contenido_json = []

        with open('extractData\\subjects.json', 'r') as file:
            contenido_json = json.load(file)
        
        for materia in contenido_json:
            if contenido_json[materia][0] == self.materia_seleccionada:
                return materia