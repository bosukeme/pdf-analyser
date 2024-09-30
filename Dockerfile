FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD [ "gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "pdfproject.wsgi:application" ]