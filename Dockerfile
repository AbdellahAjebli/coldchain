FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN addgroup --system app \
    && adduser --system --ingroup app app \
    && mkdir -p /data /app/staticfiles \
    && chown -R app:app /app /data

USER app

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && exec gunicorn projet.wsgi:application --bind 0.0.0.0:8000 --workers 2"]
