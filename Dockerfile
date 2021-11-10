FROM python:3
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt 
COPY . .   
ENV FLASK_ENV=development
ENV FLASK_APP=src/server.py
CMD flask run --host=0.0.0.0 --port=$PORT