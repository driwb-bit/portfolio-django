# 1. Usamos Python 3.12 (compatible con Django 6) en su versión ligera (slim)
FROM python:3.12-slim

# 2. Variables de entorno para optimizar Python en contenedores
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Directorio de trabajo
WORKDIR /app

# 4. Instalamos dependencias del sistema necesarias
# (gcc y librerías de imágenes para que Pillow no se rompa)
RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Copiamos los requerimientos primero (para aprovechar caché)
COPY requirements.txt /app/

# 6. Actualizamos pip e instalamos las librerías
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 7. Copiamos el resto del código del proyecto
COPY . /app/

# 8. Exponemos el puerto 8000
EXPOSE 8000

# 9. Comando para iniciar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]