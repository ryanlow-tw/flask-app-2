FROM python:3.8-slim-buster

WORKDIR /flask-app

EXPOSE 5000

COPY . .

RUN pip install -r requirements.txt


CMD ["env", "FLASK_APP=application", "python", "-m", "flask", "run", "--host=0.0.0.0"]
