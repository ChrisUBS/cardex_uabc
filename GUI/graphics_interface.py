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
        self.cb_materias = ttk.Combobox(self.ventana, values = self.materias, width = 10, font=("Inter", 18))
        self.cb_materias.place(x = 335, y = 120)

        # Botones
        #! Agregar los botones de las graficas
        self.btn_regresar = tkinter.Button(self.ventana, width = "10", text = "Regresar", font=("Inter", 20), bg = "#E4001E", fg = "white", cursor = "hand2", command=self.ventana.destroy)

        # Posicionar botones
        self.btn_regresar.place(x = 320, y = 293)

    ## Funciones de los botones ##
        
    # Botón de información
    def print_info(self):
        messagebox.showinfo("Información", 
                            "Seleccione una materia y después presione el botón de la gráfica que necesite.")