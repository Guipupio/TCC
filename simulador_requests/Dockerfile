FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /aplication
WORKDIR /aplication
COPY bot/requirements.txt /aplication/
RUN pip install -r requirements.txt
COPY bot /aplication/
CMD ["python", "/aplication/manage.py",  "runserver" ,"0.0.0.0:80"]