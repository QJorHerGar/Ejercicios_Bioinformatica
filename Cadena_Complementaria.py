import string

archivo_dna = open("pgrsequence.txt.fasta")
dna = archivo_dna.read()                           #Se abre el archivo de la cadena de DNA y se lee
byte_inicio_cadena = dna.rfind("y")                #A partir de un archivo Fasta, se encuentra donde inicia la cadena, buscando del final hacia el inicio, un espacio con rfind
archivo_dna.close()

dna = dna[byte_inicio_cadena+2: ]                          #En esta linea es desde donde se elimina todo lo que no sea la caden a de DNA
complemento = dna.maketrans("ATCG","TAGC")               #Se crea un diccionario donde cada letra del primer string, esta emparejado en posición con cada letra del segundo string
rdna = dna.translate(complemento)                        #Usando la tabla, se "traduce" cada base nitrogenada por su complemento   
rdna = rdna[::-1]                                        #Se cambia el orden, del inicio al final, ahora a ser del final al inicio. Se remplaza en el mismo objeto.

print(dna[0:20])
print(rdna[-1:-21:-1])
print(len(dna))
print(len(rdna))






