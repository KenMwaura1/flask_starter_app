FROM python:3.9.7

MAINTAINER Ken Mwaura "kemwaura@gmail.com"

COPY ./requirements.txt /app/requirements.txt

COPY . /app

WORKDIR app

ENV FLASK_APP=run.py

ENV FLASK_ENV=development

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5001:5000

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]