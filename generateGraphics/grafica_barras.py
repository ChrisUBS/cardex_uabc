class GraficaBarras:

    def __init__(self, materia_seleccionada):
        self.materia_seleccionada = materia_seleccionada

    def generar_grafica(self):
        print(f"Generando gráfica de barras de {self.materia_seleccionada}")