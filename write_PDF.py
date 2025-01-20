
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import datetime

# Este script muestra todos los datos de la secuencia analizada y crea un informe en formato .PDF

def agente_3(diccionario, nombre_fichero):  # La función recibe un diccionario con información acerca de los genes. 

    fecha_hora = datetime.datetime.now()   # Fecha y hora actual para completar el informe
    fecha_hora = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_fichero = nombre_fichero.replace(".fasta", "")  # Elimina . fasta 
    pdf_file = f"Análisis_BLAST_{nombre_fichero}.pdf"   # Crea el archivo PDF con el nombre de la tarea que hace el programa
    c = canvas.Canvas(pdf_file, pagesize=letter)


    c.setFont("Helvetica-Bold", 16)  # Tamaño y fuente
    c.setFillColor(colors.black)
    c.drawString(50, 750, "INFORME DEL ANÁLISIS DE LA SECUENCIA DE NUCLEÓTIDOS") # Título. 50 coordenada X // 750 coordenada Y

    c.setStrokeColor(colors.black)   # Agrega una línea de separación
    c.line(50, 730, 550, 730)        # Cooredenadas XY Inicio // Coordenadas XY Fin


    nombre_fichero = nombre_fichero + ".fasta"  # Vuelve a poner .fasta para que quede bonito en el informe
    c.setFont("Helvetica", 14) 
    text = f"Nombre del archivo:   {nombre_fichero}"  # Nombre del fichero analizado
    c.drawString(50, 710, text)

    text = f"Fecha y hora del análisis:   {fecha_hora}"  # Fecha y hora del análisis
    c.drawString(50, 690, text)

    c.setFont("Helvetica", 14) 
    text = f"Nº de genes encontrados: {len(diccionario)}"  # Resumen del número de genes encontrado
    c.drawString(50, 650, text)

    y_position = 620  # Posición inicial en el eje Y para comenzar a escribir.

    for key, value in diccionario.items():

        if y_position < 50:  # Si la posición en Y es menor a 50 crea una nueva página
            c.showPage() 
            y_position = 730  # Resetea la coordenada Y de nuevo a 730

        c.setFont("Helvetica", 14)  # Agrega una fuente y tamaño para el contenido del diccionario
        text = f"{key}  ......  {value}"    # Texto que escribe en cada linea
        c.drawString(50, y_position, text)   # Escribe la información del diccionario
        y_position -= 20  # Baja la posición en Y para la siguiente línea

    c.save()   # Guarda el archivo

