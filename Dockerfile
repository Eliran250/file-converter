FROM python:3.11-slim

# עדכון והתקנת libreoffice וכלים נדרשים
RUN apt-get update && apt-get install -y \
    libreoffice \
    libreoffice-writer \
    libreoffice-calc \
    libreoffice-impress \
    ghostscript \
    fonts-dejavu-core \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# התקנת תלויות Python
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# העתקת קוד הפרויקט
COPY . /app
WORKDIR /app

# פתיחת PORT
EXPOSE 8080

# פקודת הריצה – uvicorn + reload כבוי כי זה production
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
