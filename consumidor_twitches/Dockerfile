FROM ubuntu:18.04
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get update
RUN apt-get install -y python3-pip
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y stress
RUN mkdir /aplication
WORKDIR /aplication
COPY webserver/requirements.txt /aplication/
RUN pip3 install -r requirements.txt
COPY webserver /aplication/
CMD ["python3", "/aplication/manage.py",  "runserver" ,"0.0.0.0:80"]