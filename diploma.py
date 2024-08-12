import pandas as pd
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

# Leer el archivo CSV
csv_file = 'names.csv'  # Nombre de tu archivo CSV
df = pd.read_csv(csv_file)

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

# Crear un único PDF con todas las páginas
output_filename = "diplomas.pdf"
c = canvas.Canvas(output_filename, pagesize=landscape(letter))

# Crear una página en el PDF para cada nombre
for index, row in df.iterrows():
    nombre = row['Nombre']  # Ajusta si el nombre de la columna es diferente
    crear_diploma(c, nombre)

c.save()

print("Diplomas creados exitosamente.")