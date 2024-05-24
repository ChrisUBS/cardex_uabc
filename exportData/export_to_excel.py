# Librerías
from extractData.read_pdf import ReadPDF
import os
from openpyxl import Workbook
import json

class ExportToExcel():

    # Constructor
    def __init__(self, ruta_carpeta):
        self.ruta_carpeta = ruta_carpeta

        # Obtener las materias desde el archivo JSON
        self.lista_materias = []
        with open('extractData\\subjects.json', 'r') as file:
            self.lista_materias = json.load(file)

        # Crear el archivo Excel
        self.workbook = Workbook()
        self.crear_plantilla_excel()

    ### Métodos ###

    def crear_plantilla_excel(self):
        # Seleccionamos la hoja activa (por defecto, es la primera hoja)
        hoja_activa = self.workbook.active

        # Cambiamos el nombre de la hoja activa
        hoja_activa.title = 'calificaciones'

        # Datos del alumno
        hoja_activa['A1'] = 'apellido_paterno'
        hoja_activa['B1'] = 'apellido_materno'
        hoja_activa['C1'] = 'nombre'
        hoja_activa['D1'] = 'matricula'
        hoja_activa['E1'] = 'periodo'

        # Columnas de materias
        modoPasarMateria = ['_op1', '_op1_extra', '_op2', '_op2_extra', '_op3', '_op3_extra', '_acre']
        columna = 6
        for materia, formas in self.lista_materias.items():
            for modo in modoPasarMateria:
                hoja_activa.cell(row=1, column=columna, value=materia + modo)
                columna += 1

    def exportar_a_excel(self):
        # Bandera para saber si existe un PDF en la carpeta
        existsPDF = False

        # Seleccionamos la hoja activa (por defecto, es la primera hoja)
        hoja_activa = self.workbook.active

        # Contador de fila
        contadorFila = 2

        for file in os.listdir(self.ruta_carpeta):

            if file.endswith(".pdf") or file.endswith(".PDF"):
                existsPDF = True

                # Crear la ruta del PDF
                rutaPDF = self.ruta_carpeta + "/" + file
                    
                # Crear un objeto de lectura de PDF
                archivo_pdf = ReadPDF(rutaPDF)

                # Extraer datos del alumno
                nombreCompleto = archivo_pdf.obtener_nombre().split()
                matricula,periodo = archivo_pdf.obtener_matricula_y_periodo()

                # Insertar datos del alumno en la hoja de Excel
                if nombreCompleto:
                    # matricula,periodo=extracion_matricula_periodo(rutaPDF)
                    hoja_activa[f'A{contadorFila}'] = nombreCompleto[len(nombreCompleto) - 2]
                    hoja_activa[f'B{contadorFila}'] = nombreCompleto[len(nombreCompleto) - 1]
                    hoja_activa[f'C{contadorFila}'] = nombreCompleto[0]
                    hoja_activa[f'D{contadorFila}'] = matricula
                    hoja_activa[f'E{contadorFila}'] = periodo

                # Extraer las calificaciones por materia
                calificacion = []
                columna = 6
                for materia, formas in self.lista_materias.items():
                    for forma in formas:
                        calificacion = archivo_pdf.obtener_calificaciones_materia(forma)
                        if calificacion:
                            # Insertar calificaciones en la hoja de Excel
                            j = 0
                            for i in range(0, len(calificacion), 2):
                                if calificacion[i] == "ORD" and (j == 0 or j == 2 or j == 4):
                                    hoja_activa.cell(row=contadorFila, column=columna+j, value=calificacion[i+1])
                                elif calificacion[i] == "EXTRA" and (j == 1 or j == 3 or j == 5):
                                    hoja_activa.cell(row=contadorFila, column=columna+j, value=calificacion[i+1])
                                elif calificacion[i] == "ACR" and j == 6:
                                    hoja_activa.cell(row=contadorFila, column=columna+j, value=calificacion[i+1])
                                else:
                                    hoja_activa.cell(row=contadorFila, column=columna+j, value="-1")
                                j += 1
                                if j > 6:
                                    j = 0
                            break
                    
                    # Aumentamos el contador de columnas
                    columna += 6

                # Aumentamos el contador de filas
                contadorFila += 1
                            
        if existsPDF:
            # Ajustar tamaños de las columnas
            for columna in range(1, hoja_activa.max_column + 1):
                letra_columna = hoja_activa.cell(row=1, column=columna).column_letter
                hoja_activa.column_dimensions[letra_columna].width = 20

            # Guardamos el archivo Excel
            self.workbook.save(filename=self.ruta_carpeta + '/cardexUABC.xlsx')
            return True
        else:
            return False