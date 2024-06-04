# Librerías
from GUI.interface import Interface
import tkinter
from tkinter import messagebox, ttk, filedialog
import json
from exportData.export_to_csv import export_to_csv, get_ruta_carpeta
import matplotlib.pyplot as plt
from generateGraphics.grafica_barras import GraficaBarras
from generateGraphics.grafica_pastel import GraficaPastel
from generateGraphics.grafica_area import GraficaArea
from generateGraphics.grafica_barras_apiladas import GraficaBarrasApiladas

class GraphicsInterface(Interface):
    # Constante
    BG_color = "#DF9818"

    # Variable para guardar la materia seleccionada
    materia_seleccionada = ""

    # Constructor
    def __init__(self, root):
        super().__init__(root, self.BG_color)

        # Subtitulo de la ventana
        self.lbl_subtitulo = tkinter.Label(self.ventana, text = "Generar gráficas", font=("Inter", 18), bg = self.BG_color, fg = "white")
        self.lbl_subtitulo.place(x = 320, y = 85)

        # Combo box de las materias
        self.materias = self.fill_cb_materias()
        self.cb_materias = ttk.Combobox(self.ventana, values = self.materias, width = 15, font=("Inter", 18), state = "readonly", justify = "center")
        self.cb_materias.bind("<<ComboboxSelected>>", self.on_materia_selected)
        self.cb_materias.place(x=300, y=120, width=200, height=30)

        # Botones
        self.btn_graphic_barras = tkinter.Button(self.ventana, width = "15", text = "Gráfica de barras", font=("Inter", 15), bg = "black", fg = "white", cursor = "hand2", command=lambda: self.graphic_button("barras"))
        self.btn_graphic_pastel = tkinter.Button(self.ventana, width = "15", text = "Gráfica de pastel", font=("Inter", 15), bg = "black", fg = "white", cursor = "hand2", command=lambda: self.graphic_button("pastel"))
        self.btn_graphic_area = tkinter.Button(self.ventana, width = "15", text = "Gráfica de área", font=("Inter", 15), bg = "black", fg = "white", cursor = "hand2", command=lambda: self.graphic_button("area"))
        self.btn_graphic_barras_apiladas = tkinter.Button(self.ventana, width = "15", text = "Barras apiladas", font=("Inter", 15), bg = "black", fg = "white", cursor = "hand2", command=lambda: self.graphic_button("barrasapiladas"))
        self.btn_regresar = tkinter.Button(self.ventana, width = "10", text = "Regresar", font=("Inter", 20), bg = "#E4001E", fg = "white", cursor = "hand2", command=lambda: self.regresar())

        # Posicionar botones
        self.btn_graphic_barras.place(x = 200, y = 169)
        self.btn_graphic_pastel.place(x = 429, y = 169)
        self.btn_graphic_area.place(x = 200, y = 240)
        self.btn_graphic_barras_apiladas.place(x = 429, y = 240)
        self.btn_regresar.place(x = 320, y = 302)

    ## Funciones de los botones ##
        
    # Botón de información
    def print_info(self):
        messagebox.showinfo("Información",
                            "Seleccione una materia y después presione el botón de la gráfica que necesite.\n\n" +
                            "Importante:\nAntes de graficar debes extraer la información de los PDFs.")
    
    # Botón de regresar
    def regresar(self):
        plt.close() # Cerrar la ventana de la gráfica
        self.ventana.destroy()

    # Botones de las gráficas
    def graphic_button(self, tipo_grafica):
        plt.close() # Cerrar la ventana de la gráfica
        if (self.materia_seleccionada == ""):
            messagebox.showerror("Error", "Selecciona una materia.")
        elif (get_ruta_carpeta() == ""):
            messagebox.showerror("Error", "Primero extrae la información de los PDFs.")
        elif (export_to_csv() == False):
            messagebox.showerror("Error", "No se pudo acceder al archivo Excel.")
        elif (tipo_grafica == "barras"):
            GraficaBarras(self.materia_seleccionada).generar_grafica()
        elif (tipo_grafica == "pastel"):
            GraficaPastel(self.materia_seleccionada).generar_grafica()
        elif (tipo_grafica == "area"):
            GraficaArea(self.materia_seleccionada).generar_grafica()
        elif (tipo_grafica == "barrasapiladas"):
            GraficaBarrasApiladas(self.materia_seleccionada).generar_grafica()

    ## Funciones complementarias ##

    # Función para obtener la materia seleccionada
    def on_materia_selected(self, event):
        self.materia_seleccionada = self.cb_materias.get()
            
        # Obtener el ancho del combobox
        nuevo_ancho = len(self.materia_seleccionada) * 14
        if (len(self.materia_seleccionada) < 10):
            nuevo_ancho = nuevo_ancho + 40
    
        # Calcular la nueva posición del combobox para que esté centrado
        ancho_ventana = self.ventana.winfo_width()
        nueva_x = (ancho_ventana - nuevo_ancho) / 2
    
        # Modificar la posición y las dimensiones del combobox
        self.cb_materias.place(x=nueva_x, y=120, width=nuevo_ancho, height=30)

    # Función para llenar el combo box de materias
    def fill_cb_materias(self):
        contenido_json = []

        with open('extractData\\subjects.json', 'r') as file:
            contenido_json = json.load(file)

        materias = []
        
        for materia in contenido_json:
            materias.append(contenido_json[materia][0])

        return materias