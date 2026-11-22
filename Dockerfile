# Estagio 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /install
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Estagio 2: Runtime enxuto e seguro
FROM python:3.11-slim

WORKDIR /app

RUN useradd -m appuser

COPY --from=builder /install /usr/local
COPY --chown=appuser:appuser app.py .

USER appuser

EXPOSE 3000

CMD ["python", "app.py"]
