FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt && pip install --upgrade django-crispy-forms && pip install Pillow
ADD . /code/
