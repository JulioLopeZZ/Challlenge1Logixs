# Creado por Julio López López 19/01/25

#*************************************   SCRIPT PRINCIPAL   ***********************************************   

import read_FASTA
import write_PDF


archivo_fasta = input("Introduce el archivo .FASTA: ")   # Introducir el nombre del archivo .FASTA

diccionario_genes = read_FASTA.agente_1(archivo_fasta)  # Busca genes usando la herramienta BLAST. Devuelve un diccionario con el ID y los genes asociados.

write_PDF.agente_3(diccionario_genes, archivo_fasta)   # Redacta un informe con los resultados obtenidos y lo guarda en formato .PDF
