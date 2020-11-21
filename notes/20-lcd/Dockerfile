FROM python:3

COPY Adafruit_LCD1602.py /
COPY PCF8574.py /

COPY requirements.txt /
RUN pip install -r requirements.txt


COPY script.py /

CMD [ "python", "-u", "script.py" ]