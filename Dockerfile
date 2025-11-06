# Imagen base ligera
FROM python:3.12-slim

# Evita archivos .pyc y buffers
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define el directorio de trabajo
WORKDIR /app

# Copia los requerimientos
COPY requirements.txt .

# Instala dependencias del sistema necesarias para PostgreSQL y dependencias comunes
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia todo el código
COPY . .

# Exponer el puerto (Railway usará el suyo, pero esto es buena práctica)
EXPOSE 8000

# Comando de inicio (usa gunicorn con uvicorn worker)
CMD ["gunicorn", "app.main:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "[::]:8000"]
