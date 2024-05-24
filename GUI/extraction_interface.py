# Librerías
from GUI.interface import Interface
import tkinter
from tkinter import messagebox, ttk, filedialog
from threading import Thread
from exportData.export_to_excel import ExportToExcel

class ExtractionInterface(Interface):
    # Constante
    BG_color = "#1F409B"

    # Constructor
    def __init__(self, root):
        super().__init__(root, self.BG_color)

        # Ruta de la carpeta
        self.ruta_carpeta = None

        # Subtitulo de la ventana
        self.lbl_subtitulo = tkinter.Label(self.ventana, text = "Extraer la información", font=("Inter", 18), bg = self.BG_color, fg = "white")
        self.lbl_subtitulo.place(x = 292, y = 85)

        # Imagenes
        self.img_pdf = tkinter.PhotoImage(file = "GUI\\images\\pdf.png")
        self.img_pdf = self.img_pdf.subsample(12)
        self.img_flecha = tkinter.PhotoImage(file = "GUI\\images\\flecha.png")
        self.img_flecha = self.img_flecha.subsample(10)
        self.img_excel = tkinter.PhotoImage(file = "GUI\\images\\excel.png")
        self.img_excel = self.img_excel.subsample(6)
        
        # Etiquetas de las imagenes
        self.lbl_pdf = tkinter.Label(self.ventana, image = self.img_pdf, bg = self.BG_color)
        self.lbl_flecha = tkinter.Label(self.ventana, image = self.img_flecha, bg = self.BG_color)
        self.lbl_excel = tkinter.Label(self.ventana, image = self.img_excel, bg = self.BG_color)

        # Posicionar etiquetas de las imagenes
        self.lbl_pdf.place(x = 98, y = 100)
        self.lbl_flecha.place(x = 305, y = 127)
        self.lbl_excel.place(x = 566, y = 100)

        # Botones
        self.btn_seleccionar = tkinter.Button(self.ventana, width = "18", text = "Seleccionar carpeta", font=("Inter", 18), bg = "black", fg = "white", cursor = "hand2", command=self.seleccionar_carpeta)
        self.btn_exportar = tkinter.Button(self.ventana, width = "18", text = "Iniciar", font=("Inter", 18), bg = "black", fg = "white", cursor = "hand2", command=self.iniciar_exportacion)
        self.btn_regresar = tkinter.Button(self.ventana, width = "10", text = "Regresar", font=("Inter", 20), bg = "#E4001E", fg = "white", cursor = "hand2", command=self.regresar)

        # Posicionar botones
        self.btn_seleccionar.place(x = 28, y = 240)
        self.btn_exportar.place(x = 520, y = 240)
        self.btn_regresar.place(x = 320, y = 293)

    ## Funciones de los botones ##
        
    # Botón de información
    def print_info(self):
        messagebox.showinfo("Información", 
                            "Presione el botón 'Seleccionar carpeta', luego seleccione la carpeta donde se encuentran los PDFs y por último haga clic en el botón 'Iniciar'.")

    # Botón de regresar
    def regresar(self):
        try:
            if self.thread_exportar.is_alive():
                messagebox.showerror("Error", "No puedes regresar mientras se está exportando.")
            else:
                self.ventana.destroy()
        except:
            self.ventana.destroy()

    # Botón de seleccionar carpeta
    def seleccionar_carpeta(self):
        carpeta_seleccionada = filedialog.askdirectory()

        if carpeta_seleccionada:
            self.ruta_carpeta = carpeta_seleccionada
            self.btn_seleccionar.config(text = "Carpeta seleccionada", bg = "green")
        else:
            self.btn_seleccionar.config(text = "Seleccionar carpeta", bg = "black")
            self.ruta_carpeta = None

    # Botón de exportar
    def iniciar_exportacion(self):
        if self.ruta_carpeta is None:
            messagebox.showerror("Error", "Seleccione una carpeta primero.")
            return
        else:
            # Acomodar la barra de progreso
            self.btn_exportar.place_forget()
            self.btn_seleccionar.config(state="disabled", width = "20", text="Procesando...", bg="black", fg="white", font=("Inter", 15))
            self.progressbar = ttk.Progressbar(self.ventana, mode="indeterminate")
            self.progressbar.place(x = 590, y = 245, width=120, height=30)
            self.progressbar.start(10)

            # Iniciar el hilo de exportación
            self.thread_exportar = Thread(target=self.hilo_exportar)
            if not self.thread_exportar.is_alive():
                self.thread_exportar.start()

    def hilo_exportar(self):
        try:
            # Crear el objeto de exportación
            archivo_excel = ExportToExcel(self.ruta_carpeta)

            # Exportar calificaciones y obtener el estado
            estado_exportar = archivo_excel.exportar_a_excel()
        
            # Detener la barra de progreso y acomodar todo
            if self.progressbar:
                self.progressbar.destroy()
                self.btn_exportar.place(x = 520, y = 240)
                self.btn_seleccionar.config(state="normal", width = "18", text = "Seleccionar carpeta", font=("Inter", 18), bg = "black", fg = "white")

            if estado_exportar:
                messagebox.showinfo("Éxito", "Exportación completada.")
            else:
                messagebox.showerror("Error", "No se encontraron archivos PDF en la carpeta seleccionada.")
            
            self.ruta_carpeta = None
            return
            
        except:
            # Detener la barra de progreso y acomodar todo
            if self.progressbar:
                self.progressbar.destroy()
                self.btn_exportar.place(x = 520, y = 240)
                self.btn_seleccionar.config(state="normal", width = "18", text = "Seleccionar carpeta", font=("Inter", 18), bg = "black", fg = "white")

            messagebox.showerror("Error", "Ocurrió un error al exportar las calificaciones.\n" +
                                 "Revisa tus archivos PDF y/o asegurate de que el archivo Excel no esté abierto.")
            self.ruta_carpeta = None
            return