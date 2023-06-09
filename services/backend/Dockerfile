# pull official base image
FROM python:3.11-buster

# set work directory
RUN mkdir app
WORKDIR /app

# set environment variables
ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.
# ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY src/ .