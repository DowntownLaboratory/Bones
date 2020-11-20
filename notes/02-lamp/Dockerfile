FROM python:3

COPY lamp.py /
COPY requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "-u", "lamp.py" ]