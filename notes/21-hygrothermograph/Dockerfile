FROM python:3

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY Freenove_DHT.py / 
COPY script.py /

CMD [ "python", "-u", "script.py" ]