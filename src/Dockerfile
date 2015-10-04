FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:3000 app:app
