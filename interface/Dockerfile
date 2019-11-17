FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /aplication
RUN mkdir /aplication/chaos-outputs
WORKDIR /aplication
COPY webserver/requirements.txt /aplication/
RUN pip install -r requirements.txt
COPY webserver /aplication/
CMD ["python", "/aplication/manage.py",  "runserver" ,"0.0.0.0:80"]