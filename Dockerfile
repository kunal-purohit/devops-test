FROM python:latest

COPY requirements.txt requirements.txt

RUN pip install --no-cache -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]