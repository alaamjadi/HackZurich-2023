FROM python:3.11
COPY app /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["tail", "-f", "/dev/null" ]
CMD ["python", "crawler.py"]
