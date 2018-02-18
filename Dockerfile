FROM python:2-jessie
MAINTAINER Piotr Karpala

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["hello.py"]
