FROM python:3
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt 
COPY . .   
EXPOSE 5000 
ENV FLASK_ENV=development
CMD ["FLASK_APP=src/server.py","flask run"]