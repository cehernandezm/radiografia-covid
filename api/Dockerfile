FROM python:latest

EXPOSE 4200

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "index.py" ]