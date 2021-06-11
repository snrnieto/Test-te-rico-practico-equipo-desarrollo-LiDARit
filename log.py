import sys

log= sys.argv[1]
archivo_entrada=sys.argv[2]
archivo_salida=sys.argv[3]


f = open(archivo_entrada, "r")

texto_salida=""

for x in f:
  if log.upper() in x:
     texto_salida+=x

text_file = open(archivo_salida, "w")
text_file.write(texto_salida)
text_file.close()
