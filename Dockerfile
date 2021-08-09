FROM datamechanics/spark:3.1-latest

WORKDIR /flask-app

EXPOSE 5000

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["env", "FLASK_APP=application", "python3", "-m", "flask", "run", "--host=0.0.0.0"]
