FROM python:3

COPY blink.py /
COPY requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "-u", "blink.py" ]