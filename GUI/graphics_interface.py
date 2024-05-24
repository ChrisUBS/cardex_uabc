# Librerías
from GUI.interface import Interface
import tkinter
from tkinter import messagebox, ttk, filedialog

class GraphicsInterface(Interface):
    # Constante
    BG_color = "#DF9818"

    # Constructor
    def __init__(self, root):
        super().__init__(root, self.BG_color)

        # Subtitulo de la ventana
        self.lbl_subtitulo = tkinter.Label(self.ventana, text = "Generar gráficas", font=("Inter", 18), bg = self.BG_color, fg = "white")
        self.lbl_subtitulo.place(x = 320, y = 85)

        # Combo box de las materias
        self.materias = ["Materia 1", "Materia 2", "Materia 3", "Materia 4", "Materia 5"]
        self.cb_materias = ttk.Combobox(self.ventana, values = self.materias, width = 15, font=("Inter", 18))
        self.cb_materias.place(x = 300, y = 120)

        # Botones
        self.btn_graphic_barras = tkinter.Button(self.ventana, width = "15", text = "Gráfica de barras", font=("Inter", 15), bg = "black", fg = "white", cursor = "hand2")
        self.btn_graphic_pastel = tkinter.Button(self.ventana, width = "15", text = "Gráfica de pastel", font=("Inter", 15), bg = "black", fg = "white", cursor = "hand2")
        self.btn_graphic_poligonal = tkinter.Button(self.ventana, width = "15", text = "Gráfica poligonal", font=("Inter", 15), bg = "black", fg = "white", cursor = "hand2")
        self.btn_graphic_lineal = tkinter.Button(self.ventana, width = "15", text = "Gráfica lineal", font=("Inter", 15), bg = "black", fg = "white", cursor = "hand2")
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
                            "Seleccione una materia y después presione el botón de la gráfica que necesite.")