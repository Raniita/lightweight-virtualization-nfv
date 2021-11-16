# Un Dockerfile siempre necesita importar una imagen como base
# Para ello utilizamos 'FROM'
# Elegimos 'python' para la imagen y 'latest' como version de esa imagen
FROM python:latest

# Para ejecutar nuestro codigo Python, lo copiamos dentro del contenedor
# Para ello utilizamos 'COPY'
# El primer parametro 'main.py' es la ruta origen del archivo en el host
# El segundo parametro '/' es la ruta destino del archivo dentro del contenedor
# En este caso, ponemos el archivo en el root del sistema
COPY main.py /

# Definimos el comando a ejecutar cuando iniciemos el contenedor
# Para ello utilizamos 'CMD'
# Para ejecutar la aplicacion utilizariamos "python ./main.py".
CMD [ "python", "./main.py" ]
