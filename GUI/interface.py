# Librerías
from abc import ABC, abstractmethod
import tkinter

class Interface(ABC):
    # Constantes
    WIDTH = "800"
    HEIGHT = "400"

    # Variables globales
    root = None

    # Constructor
    def __init__(self, root, BG_color):
        self.root = root

        # Ajustes de la ventana
        self.ventana = self.root
        self.ventana.title("Cardex UABC")
        self.ventana.geometry(self.WIDTH + "x" + self.HEIGHT)
        self.ventana.resizable(False, False)
        self.ventana.config(bg = BG_color)
        self.ventana.iconbitmap("GUI\\images\\app_icon.ico")
        self.centrar_ventana()

        # Etiqueta título
        self.lbl_titulo = tkinter.Label(self.ventana, text = "Cardex UABC", font=("Inter", 40, "bold"), bg = BG_color, fg = "white")
        self.lbl_titulo.place(x = 230, y = 30)

        # Botón de información
        self.img_info = tkinter.PhotoImage(file = "GUI\\images\\info_icon.png")
        self.img_info = self.img_info.subsample(10)
        self.btn_info = tkinter.Button(self.ventana, image = self.img_info, bg = BG_color, bd = 0, cursor = "hand2",command = self.print_info)
        self.btn_info.place(x = 10, y = 10)

        # Etiqueta de pie de página
        self.lbl_footer = tkinter.Label(self.ventana, text = "©2024 Todos los derechos reservados.", font=("Inter", 10), bg = BG_color, fg = "white")
        self.lbl_footer.place(x = 290, y = 360)
        
    # Función del botón de información
    @abstractmethod
    def print_info(self):
        pass

    # Centrar ventana en la pantalla
    def centrar_ventana(self):
        self.ventana.update_idletasks()
        ancho_ventana = self.ventana.winfo_width()
        alto_ventana = self.ventana.winfo_height()
        x_ubicacion = (self.ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y_ubicacion = (self.ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
        self.ventana.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x_ubicacion, y_ubicacion))