# Diplomas para Git Commit

Este proyecto fue creado para automatizar la generación de diplomas para GitCommit, asegurando que no sea necesario recordar cada año cómo hacerlo. Con este repositorio, podrás generar e imprimir diplomas de manera sencilla utilizando un archivo CSV con los nombres de las escuelas y los participantes. El repositorio está preparado para ejecutarse en un GitHub Codespace, con todas las dependencias ya configuradas, para que no tengas que instalar nada adicional.

## Descripción del Proyecto

Los diplomas se generan a partir de un archivo CSV que contiene los nombres de las escuelas y los nombres de los participantes.

- **Importante:** Este repositorio está diseñado para que funcione en un Codespace, asegurando que todas las dependencias estén instaladas automáticamente.
- **Formato del Diploma:** Los diplomas están configurados para imprimirse en tamaño carta, con un espacio reservado para la imagen y el nombre del participante en una posición específica.

<img src="https://github.com/user-attachments/assets/e4c11d16-21ee-4609-a45d-b28f16ed41f3" alt="diploma" width="600">

## Requisitos Previos

No necesitas instalar nada si utilizas un Codespace. Sin embargo, si deseas ejecutar el código localmente, deberás cumplir con los siguientes requisitos:

- **Python 3.11**
- **Dependencias:** Pandas, ReportLab

**Recomendación:** Ejecutar el código en un Codespace para evitar configuraciones manuales.

## Configuración y Uso

Sigue estos pasos para generar los diplomas:

1. **Iniciar Codespace:**
   - Haz clic en el botón **Codespaces** en la página del repositorio.
   - Selecciona la rama adecuada y comienza un Codespace.
   - Una vez cargado, todas las dependencias estarán listas para usar.

<img src="https://github.com/user-attachments/assets/303e81b2-22e0-4559-8ad2-3cf29fc98b17" alt="Iniciar Codespace" width="600">

2. **Preparar el Archivo CSV:**
   - Abre el archivo `names.csv` en el Codespace.
   - Este archivo contiene los nombres de las escuelas y los alumnos. Para facilitar la creación de este archivo, puedes utilizar [este Google Spreadsheet](https://docs.google.com/spreadsheets/d/1YrMRFIoYCjaNKyiqnoLofLwByO8FeLyJqR5N4Jznr1k/edit?gid=0#gid=0) que te permite organizar y generar los nombres y escuelas correctamente.
   - En el Google Spreadsheet, selecciona la columna que contiene la combinación de la escuela y el nombre.
   - Copia y pega estos datos en el archivo `names.csv`, sustituyendo los nombres de ejemplo.

<img src="https://github.com/user-attachments/assets/9f2d6ee0-445d-4757-b63c-90c329336a52" alt="Preparar el archivo CSV" width="600">

3. **Ejecutar el Código:**
   - Una vez que los nombres estén en el archivo `names.csv`, abre la terminal en Codespace.
   - Escribe `python diplomas.py` y presiona Enter.
   - En pocos segundos, verás un mensaje confirmando que los diplomas se han creado correctamente.

<img src="https://github.com/user-attachments/assets/d88c75c3-8344-4c6f-913e-281befe446da" alt="Ejecutar el código" width="600">

4. **Revisar y Descargar los PDFs:**
   - En el Codespace, se generará una carpeta llamada `PDFs para imprimir`.
   - Dentro de esta carpeta, encontrarás un archivo PDF por cada escuela, con los nombres de los estudiantes listos para imprimir.

## Notas para la Impresión

- **Impresión en Impulso:**
  - Los diplomas se imprimen en la biblioteca de Impulso, utilizando una fotocopiadora en blanco y negro.
  - Asegúrate de configurar la impresora para utilizar la bandeja manual y seleccionar tamaño carta como origen.
  - Es importante tener los diplomas preimpresos en tamaño carta para que el texto se alinee correctamente.

## Personalización del Diploma

- **Ajustes en el Diseño:**
  - El diseño del diploma puede cambiarse sin ningún problema, siempre y cuando la posición y el tamaño del área destinada para el nombre permanezcan igual.
  - Las coordenadas actuales están configuradas específicamente para imprimir el nombre en un diploma de tamaño carta. Si decides cambiar el diseño, asegúrate de que el espacio destinado al nombre no cambie de lugar ni de tamaño.
  - **Recomendación:** Mantén el área donde se imprime el nombre en la misma posición para evitar problemas con la impresión. El resto del diseño del diploma puede modificarse según sea necesario, y esto no afectará la impresión correcta de los nombres.
