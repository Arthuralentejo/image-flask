FROM python:3

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install

RUN apt-get install tesseract-ocr -y &&\
    apt-get install tesseract-ocr-por

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "./app.py" ]