FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

VOLUME /app
WORKDIR /app
EXPOSE 80
ENTRYPOINT [ "python3" ]
CMD ["consumer.py" ]

