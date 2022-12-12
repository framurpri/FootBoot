# Especificamos la imagen base que vamos a utilizar para nuestro contenedor
FROM python:3.8

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos todos los archivos del directorio actual en el contenedor
COPY . /app

# Instalamos las dependencias de nuestro proyecto Django
RUN pip install -r requirements.txt

# Exponemos el puerto 8000 del contenedor para que podamos acceder a nuestra aplicación Django
EXPOSE 8000

# Establecemos una variable de entorno con el nombre de nuestra aplicación Django
ENV DJANGO_APP_NAME=footboot

# Establecemos una variable de entorno con la ruta de nuestro archivo manage.py
ENV DJANGO_MANAGE_FILE=./app/manage.py

# Establecemos la orden que se ejecutará cuando se inicie el contenedor
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]