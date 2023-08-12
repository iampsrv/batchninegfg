FROM python:3.12.0b3-alpine3.18
COPY . /application
WORKDIR /application
COPY req.txt .
RUN pip install -r req.txt
EXPOSE 5001
CMD ["python", "app.py"]
