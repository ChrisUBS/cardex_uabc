import matplotlib.pyplot as plt

class GraficaLineal:

    def __init__(self, materia_seleccionada):
        self.materia_seleccionada = materia_seleccionada

    def generar_grafica(self):

        # Datos
        categorias = ['A', 'B', 'C', 'D', 'E']
        valores = [5, 7, 3, 8, 4]

        # Crear el gráfico de barras
        plt.bar(categorias, valores)

        # Añadir título y etiquetas
        plt.title(self.materia_seleccionada)
        plt.xlabel("Categorías")
        plt.ylabel("Valores")

        # Mostrar el gráfico
        plt.show()