FROM python:3.8-slim
WORKDIR /app

COPY ./python-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY python-app/ .

EXPOSE 5000
CMD [ "python", "main.py" ]
