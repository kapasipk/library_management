# Pull base image
FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /code
RUN pip3 install django
WORKDIR /code

# Install dependencies

#Upgrade pip
RUN pip install pip -U
ADD requirements.txt /code/

#Install dependencies
RUN pip install -r requirements.txt
ADD . /code/
