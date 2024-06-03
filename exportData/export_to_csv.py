# Librerías
import pandas as pd

# Variable global
carpeta_ruta = ""# Especificar las rutas de los archivos

def set_ruta_carpeta(ruta):
    global carpeta_ruta
    carpeta_ruta = ruta

def get_ruta_carpeta():
    return carpeta_ruta

# Exportar a CSV
def export_to_csv():
    ruta_archivo_excel = carpeta_ruta + '/cardexUABC.xlsx'
    ruta_archivo_csv = carpeta_ruta + '/cardexUABC.csv'

    try:
        # Lee el archivo Excel
        df = pd.read_excel(ruta_archivo_excel)

        # Guarda el DataFrame como un archivo CSV
        df.to_csv(ruta_archivo_csv, index=False)

        return True
    except:
        return False