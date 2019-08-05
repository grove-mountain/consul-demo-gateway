FROM python:alpine

RUN pip install --no-cache-dir Flask requests \
  && mkdir /app

ADD app/ app/

WORKDIR /app

# The internal port for the application
EXPOSE 8000

ENTRYPOINT ["python","app.py"]
