# Python imajını kullan
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gerekli bağımlılıkları yükle
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Flask uygulamasını kopyala
COPY . .

# Uygulamayı başlat
CMD ["python", "app.py"]
