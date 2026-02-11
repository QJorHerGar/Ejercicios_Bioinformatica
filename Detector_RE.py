import re

archivo_dna = open("pgrsequence.txt.fasta")
dna = archivo_dna.read()                                          #Se abre el archivo de la cadena de DNA y se lee
byte_inicio_cadena = dna.rfind("y")                               #A partir de un archivo Fasta, se encuentra donde inicia la cadena, que es donde termina la palabra "assembly" 
archivo_dna.close()                                               #ERROR Falta sacar todo lo que no sean nucleatidos :C

dna = dna[byte_inicio_cadena+2: ] 

PRE = "ACAxxxTGT"
ERE = "GGTCAxxxTGACC"

def read_ERE(dna):
    posicionesPRE = []                                                    #Elementos de REspuesta a Estrogenos
    for i in range(0,len(dna)-99,100):
        segmento = dna[i:i+99]
        posicion = segmento.find("ACA")
        if posicion != -1 and (posicion + i + 9 <= len(dna)) and (dna[i + posicion + 6:i + posicion + 9] == "TGT"):
            posicionesPRE.append(i + posicion)                             #ERROR: Se ignora que los elementos de respuesta, podrian quedar entre los segmentos.
        continue    
    return posicionesPRE

def read_PRE(dna):
    posicionesERE = []        #Elementos de Respuesta a Progesterona
    for i in range(0,len(dna)-99,100):
        segmento = dna[i:i+99]
        posicion = segmento.find("GGTCA")
        if posicion != -1 and (posicion + i + 13 <= len(dna)) and (dna[i + posicion + 8:i + posicion + 13] == "TGACC"):
            posicionesERE.append(i + posicion)
        continue
    return posicionesERE

