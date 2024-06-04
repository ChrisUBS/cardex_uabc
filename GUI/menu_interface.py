from GUI.interface import Interface
from GUI.extraction_interface import ExtractionInterface
from GUI.graphics_interface import GraphicsInterface
import tkinter
from tkinter import messagebox

class MenuInterface(Interface):
    # Constante
    BG_color = "#00733F"

    # Constructor
    def __init__(self, root):
        super().__init__(root, self.BG_color)

        # Logo de la UABC
        self.img_uabc = tkinter.PhotoImage(file = "GUI\\images\\uabc_logo.png")
        self.img_uabc = self.img_uabc.subsample(2)
        self.lbl_uabc = tkinter.Label(self.ventana, image = self.img_uabc, bg = self.BG_color)
        self.lbl_uabc.place(x = 147, y = 88)

        # Botones
        self.btn_extraccion = tkinter.Button(self.ventana, width = "15", text = "Extraer información", font=("Inter", 20), bg = "black", fg = "white", cursor = "hand2", command=self.abrir_ventana_extraccion)
        self.btn_graficas = tkinter.Button(self.ventana, width = "15", text = "Generar gráficas", font=("Inter", 20), bg = "black", fg = "white", cursor = "hand2", command=self.abrir_ventana_graficas)
        self.btn_salir = tkinter.Button(self.ventana, width = "15", text = "Salir", font=("Inter", 20), bg = "#E4001E", fg = "white", cursor = "hand2", command=self.ventana.destroy)

        # Posicionar botones
        self.btn_extraccion.place(x = 430, y = 110)
        self.btn_graficas.place(x = 430, y = 181)
        self.btn_salir.place(x = 430, y = 252)

    ## Funciones de los botones ##
        
    # Botón de información
    def print_info(self):
        messagebox.showinfo("Información", 
                            "Cárdex UABC es una aplicación que permite extraer las calificaciones de los cárdex de la UABC, exportarlas a un archivo de Excel y generar gráficas con los datos.\n" +
                            "\nDesarrollado por: \n- Christian Uriel Bonilla Suárez\n- Jose Eduardo Becerra Flores\n\nVersión: 2.0")
        
    # Botón de extracción
    def abrir_ventana_extraccion(self):
        self.ventana.withdraw()
        extraction_app = ExtractionInterface(tkinter.Toplevel())   
        self.ventana.wait_window(extraction_app.ventana)
        self.ventana.deiconify()

    # Botón de gráficas
    def abrir_ventana_graficas(self):
        self.ventana.withdraw()
        graphics_app = GraphicsInterface(tkinter.Toplevel())
        self.ventana.wait_window(graphics_app.ventana)
        self.ventana.deiconify()