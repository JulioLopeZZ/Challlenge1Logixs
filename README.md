## Resumen

Este proyecto permite analizar una secuencia de nucleótidos de un fichero .fasta y poder obtener los genes asociados a dicha secuencia junto a su identificador. Para ello se hace uso de la tecnología BLAST que permite comparar la secuencia frente a una gran base de datos genómica. Además genera de manera automática un informe .PDF con los datos básicos de la consulta.


## Estructura del proyecto

/Challenge1Logix

|-- README.md                      # Es este archivo

|-- requirements.txt               # Lista de dependencias

|-- main.py                        # Archivo principal

|-- read_FASTA.py                  # Función encargada de leer y buscar genes

|-- write_PDF.py                   # Función encargada de generar un PDF con los resultados

|-- sample.fasta                   # Archivo .FASTA de prueba

|-- seq_nuc.fasta                  # Archivo .FASTA de prueba

|-- Análisis_BLAST_sample.pdf      # Archivo .PDF generado

|-- Análisis_BLAST_seq_nuc.pdf     # Archivo .PDF generado 



## Instalación

    1. Clonar el entorno virtual:

    -->> git clone https://github.com/JulioLopeZZ/Challlenge1Logixs.git


    2. Acceso a la carpeta del proyecto:

    -->> cd Challlenge1Logixs


    3. (Opcional) Crea un entorno virtual para aislar las dependencias:

    -->> python3 -m venv venv


    4. Activar el entorno virtual:

    -->> venv\Scripts\activate


    5. Instalar dependencias:

    -->> pip install -r requirements.txt

## Uso

Para ejecutar el proyecto hay que utilizar el archivo principal main.py:

-->>  python main.py

Para su utilización se debe de introducir manualmente el nombre del fichero .FASTA. EL tiempo de análisis es de aproximadamente 1 minuto por lo que hay que tener paciencia.
