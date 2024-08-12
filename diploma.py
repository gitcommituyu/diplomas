import pandas as pd
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

# Leer el archivo CSV
csv_file = 'names.csv'  # Nombre de tu archivo CSV
df = pd.read_csv(csv_file)

# Asegúrate de que la carpeta para los PDFs exista
output_dir = 'PDFs para imprimir'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Definir la función para crear el PDF
def crear_diploma(c, nombre):
    # Ruta a la fuente Arial
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # Cambia esto a la ruta de Arial si la tienes
    if os.path.exists(font_path):
        pdfmetrics.registerFont(TTFont('Arial', font_path))
        c.setFont("Arial", 20)
    else:
        c.setFont("Helvetica", 20)  # Fuente predeterminada

    # Agregar el nombre en una posición específica
    x = 75
    y = 335
    c.drawString(x, y, nombre)
    
    c.showPage()

# Agrupar por escuela
escuelas = df.groupby('escuela')

# Crear un PDF por escuela
for nombre_escuela, grupo in escuelas:
    output_filename = os.path.join(output_dir, f"{nombre_escuela}.pdf")
    c = canvas.Canvas(output_filename, pagesize=landscape(letter))
    
    # Crear una página en el PDF para cada alumno de la escuela
    for index, row in grupo.iterrows():
        nombre_alumno = row['nombre']
        crear_diploma(c, nombre_alumno)
    
    c.save()

print("PDFs creados exitosamente en la carpeta 'PDFs para imprimir'.")