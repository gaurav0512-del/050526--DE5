FROM python:3.12-slim
WORKDIR /app
RUN pip install pandas
COPY clean.py .
COPY . /app
ENTRYPOINT ["python","clean.py"]