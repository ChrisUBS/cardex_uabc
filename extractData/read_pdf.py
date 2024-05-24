# Librerías
import PyPDF2
import re

class ReadPDF():

    # Constructor
    def __init__(self, pathPDF):
        self.pathPDF = pathPDF

        #Abrimos el PDF
        self.pdf_file = open(pathPDF, 'rb')
        self.pdf_reader = PyPDF2.PdfReader(self.pdf_file)

        # # Abrimos el PDF
        # self.pdf_reader = PyPDF2.PdfFileReader(open(self.pathPDF, 'rb'))

    ### Métodos ###

    def obtener_nombre(self):
        
        # Extraemos la informacion de la primera pagina
        page = self.pdf_reader.pages[0]

        # Transcribimos todo el texto de la primera pagina
        texto = page.extract_text()

        # Variable donde se almacenara el nombre completo de cada alumno
        nombre = ""

        # Dividimos todo el PDF en lineas
        for linea in texto.splitlines():
            
            # Si en la linea donde estamos, contiene la palabra "Asig"
            # Ahi es donde se encuentra el nombre completo de la persona
            if re.search(r"\bAsig\b",linea):

                # Recortamos la linea de nuestro documento, omitiendo todo hasta el nombre
                nombre = linea[10:]

        # Cuando terminemos de leer las lineas, retornamos el nombre
        return nombre
    
    def obtener_matricula_y_periodo(self):

        # Extraemos la informacion de la primera pagina
        page = self.pdf_reader.pages[0]

        # Transcribimos todo el texto de la primera pagina
        texto = page.extract_text()

        # Variable donde se almacenara el nombre completo de cada alumno
        matricula = ""
        periodo=""

        # Dividimos todo el PDF en lineas
        for linea in texto.splitlines():

            if re.search(r"\bPlan de Estudios\b",linea):
                pos=linea.find("Plan de Estudios")
                matricula = linea[0:pos-1]
                periodo = linea[pos+18:]
    
        # Cuando terminemos de leer las lineas, retornamos el nombre
        return matricula, periodo

    def obtener_calificaciones_materia(self, materia):

        # Extraemos la informacion de la primera pagina
        page = self.pdf_reader.pages[0]

        # Transcribimos todo el texto de la primera pagina
        texto = page.extract_text()

        # Arreglo para guardar todas las calificaciones encontradas de la materia en concreto
        calificaciones=[]

        # Dividimos todo el PDF en lineas
        for linea in texto.splitlines():
            
            # Si en la linea donde estamos, contiene el nombre de la materia que buscamos, vamos a extraer la informacion
            if re.search(materia,linea):
                
                # Creamos un arreglo para guardar cada digito de la calificacion por separado
                calificacion_partida = []

                # IF para buscar si el alumno paso la materia en ORDINARIO
                if linea.find("Ord") != -1:
                    pos = linea.find("Ord") # Ver en que posicion se encuentra la palabra ORD
                    calificaciones.append("ORD")

                # IF para buscar si el alumno paso la materia en EXTRAORDINARIO
                elif linea.find("Ext") != -1:
                    pos = linea.find("Ext")
                    calificaciones.append("EXTRA") # Ver en que posicion se encuentra la palabra EXTRA
                
                # IF para buscar si el alumno paso la materia en ACREDITACION
                elif linea.find("Acr") != -1:
                    pos = linea.find("Acr") # Ver en que posicion se encuentra la palabra ACR
                    calificaciones.append("ACR")
        
                # Recortamos la linea de nuestro documento, omitiendo todo hasta la calificacion
                linea_rec = linea[pos+4:] 

                # Ciclo para buscar todos los digitos de la calificacion
                for caracter in linea_rec:
                    #Si el caracter no es un espacio, seguimos agregando calificaciones al arreglo
                    if caracter!=" ":
                        calificacion_partida.append(caracter)
                    #Si encontramos un espacio, se termina el ciclo
                    else:
                        break

                # Funcion para unir todos los digitos de la calificacion, en un solo numero
                numeros = ''.join(calificacion_partida) 
                # Agregamos la calificaciones al arreglo principal
                calificaciones.append(numeros)

        # Cuando terminemos de leer las lineas, retornamos el arreglo con calificaciones
        return calificaciones