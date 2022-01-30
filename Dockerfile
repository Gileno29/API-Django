FROM python:3.10
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  EXPOSE 8000
  ENV PYTHONDONTWRITEBYTECODE=1
  ENV PYTHONUNBUFFERED=1
  COPY . .
  