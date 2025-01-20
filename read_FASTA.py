from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.Blast import NCBIXML
import requests

# Este script lee un archivo .FASTA y devuelve los nombres y los ID de los posibles genes asociados a la secuencia de nucleótidos

def agente_1(archivo_fasta):
    
    lista_genes = []   # Lista en donde se muestran los diferentes genes asociados a la secuencia

    diccionario_id_gen = {}   # Diccionario "id_gen" : "nombre_completo_gen"

    secuencia = SeqIO.read(archivo_fasta, "fasta")   # Leer una secuencia en formato FASTA desde un archivo

    resultados_blast = NCBIWWW.qblast("blastn", "nt", secuencia.seq)   # Realizar la búsqueda BLAST en el servidor de NCBI (pidiendo una búsqueda en la base de datos 'nt' - nucleótidos)
    
    blast_records = NCBIXML.parse(resultados_blast)   # Analizar los resultados de BLAST directamente 

    for blast_record in blast_records:   # Mostrar la información de los alineamientos

        for alignment in blast_record.alignments:
            lista_genes.append(alignment.accession)   # Nos da el ID del cada gen de la alineación en formato "nuevo"
                              
    if len(lista_genes) == 0:

        return diccionario_id_gen
    
    else:
        
        #lista_genes = lista_genes[:10]   Limita la búsqueda a los 10 mejores alineamientos. SE PUEDE ACTIVAR SI SE DESEA

        for gen_id in lista_genes:
            url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nucleotide&id={gen_id}&retmode=json"   # URL de la API de Entrez en NCBI
            response = requests.get(url)   # Realizar la solicitud GET
            datos = response.json()   #  Devuelve un JSON de donde se extraerán datos.

            if response.status_code == 200:
                clave = datos["result"]["uids"]          # Con esto se saca el nombre completo del gen asociado al ID
                clave = clave[0]
                nombre_completo = datos["result"][clave]["title"]
                nombre_completo = nombre_completo.split(",")  # Divide por comas para acortar el nombre del gen
                nombre_completo = nombre_completo[0]          #Se queda solo con el primer valor de la lista que es el nombre del gen que nos interesa
                diccionario_id_gen[gen_id] = nombre_completo
        
            else:  
                raise SystemExit   # Finaliza el programa al no encontrar una respuesta a la consulta de la API
                    
    return diccionario_id_gen 




