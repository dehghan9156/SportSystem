FROM python:3.10

WORKDIR /code
COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/
EXPOSE 8000

CMD [ "gunicorn","sportsystem.wsgi",":8000" ]
