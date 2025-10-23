# Imagen base con Python 3.10 (puede ser 3.11 también)
FROM python:3.10-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos del proyecto al contenedor
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000 (Flask por defecto)
EXPOSE 5000

# Definir variable de entorno para Flask
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Comando para ejecutar la aplicación
CMD ["flask", "run"]
