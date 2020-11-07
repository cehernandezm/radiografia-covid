FROM python:3.7-slim

EXPOSE 4200

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "index.py" ]