# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim
FROM python:3.8
COPY ./ /app
WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt


# RUN apt-get install gcc
# RUN apt-get install g++

RUN tar -xzf ta-lib-0.4.0-src.tar.gz
RUN cd ta-lib && ./configure 
RUN cd ta-lib && make 
RUN cd ta-lib && make install 
RUN cd ta-lib && pip install TA-Lib

EXPOSE 80

CMD [ "uvicorn", "main:app","--host=0.0.0.0", "--port=80", "--reload", "--workers", "33" ]