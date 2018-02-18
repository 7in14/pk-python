FROM python:2-jessie
MAINTAINER Piotr Karpala
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["hello.py"]
