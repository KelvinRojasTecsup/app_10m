# Usa una imagen de Python como base
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el script Python y el archivo de requisitos al contenedor
COPY consume_api.py .

# Instala las bibliotecas necesarias
RUN pip install requests

# Comando para ejecutar el script
CMD ["python", "./consume_api.py"]
