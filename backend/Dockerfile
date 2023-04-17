FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

COPY ./ /app
WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements_docker.txt

EXPOSE 80

CMD [ "uvicorn", "main:app","--host=0.0.0.0", "--port=80", "--reload", "--workers", "33" ]


