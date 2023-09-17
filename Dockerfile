FROM python:3.10
COPY app /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["tail", "-f", "/dev/null" ]
CMD ["python", "crawler.py"]


# update: added instructions
# docker build -t crawler .
# docker run -v ./files:/files -v ./results:/results --network none crawler

# get shell
# docker exec -it crawler /bin/bash
