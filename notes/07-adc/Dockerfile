FROM python:3

COPY ./ADCDevice-1.0.3 /
RUN python3 setup.py install

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY script.py /
CMD [ "python", "-u", "script.py" ]