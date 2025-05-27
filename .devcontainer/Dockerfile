# Imagen base con Python 3.10 (compatible con TensorFlow)
FROM python:3.10-slim

# Evita prompts de instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean

# Crea el directorio de la app
WORKDIR /workspace

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
