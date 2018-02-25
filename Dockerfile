FROM python:3.6.4-slim-jessie
MAINTAINER Piotr Karpala
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
