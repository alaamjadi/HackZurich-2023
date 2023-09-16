FROM python:3.11
COPY app /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python", "crawler.py"]