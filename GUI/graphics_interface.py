# Librerías
from GUI.interface import Interface
import tkinter
from tkinter import messagebox, ttk, filedialog
import json
from generateGraphics.grafica_barras import GraficaBarras

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
        self.btn_graphic_poligonal = tkinter.Button(self.ventana, width = "15", text = "Gráfica poligonal", font=("Inter", 15), bg = "black", fg = "white", cursor = "hand2", command=lambda: self.graphic_button("poligonal"))
        self.btn_graphic_lineal = tkinter.Button(self.ventana, width = "15", text = "Gráfica lineal", font=("Inter", 15), bg = "black", fg = "white", cursor = "hand2", command=lambda: self.graphic_button("lineal"))
        self.btn_regresar = tkinter.Button(self.ventana, width = "10", text = "Regresar", font=("Inter", 20), bg = "#E4001E", fg = "white", cursor = "hand2", command=self.ventana.destroy)

        # Posicionar botones
        self.btn_graphic_barras.place(x = 200, y = 169)
        self.btn_graphic_pastel.place(x = 429, y = 169)
        self.btn_graphic_poligonal.place(x = 200, y = 240)
        self.btn_graphic_lineal.place(x = 429, y = 240)
        self.btn_regresar.place(x = 320, y = 302)

    ## Funciones de los botones ##
        
    # Botón de información
    def print_info(self):
        messagebox.showinfo("Información",
                            "Seleccione una materia y después presione el botón de la gráfica que necesite.\n\n" +
                            "Importante:\nAntes de graficar debes extraer la información de los PDFs.")
    
    # Botones de las gráficas
    def graphic_button(self, tipo_grafica):
        if (self.materia_seleccionada == ""):
            messagebox.showerror("Error", "Selecciona una materia.")
        elif (tipo_grafica == "barras"):
            GraficaBarras(self.materia_seleccionada).generar_grafica()
        elif (tipo_grafica == "pastel"):
            pass
        elif (tipo_grafica == "poligonal"):
            pass
        elif (tipo_grafica == "lineal"):
            pass

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