FROM python:3.7-slim

EXPOSE 5000

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "index.py" ]