# Fetching official base image for python
FROM python:3.9.6-alpine

# Setting up the work directory
WORKDIR /src

# Preventing python from writing
# pyc to docker container
ENV PYTHONDONTWRITEBYTECODE 1

# for setting python output directly to the terminal with out buffering
ENV PYTHONUNBUFFERED 1

# Updating the os
RUN apk update 

# Installing python3
RUN apk add python3-dev

# Copying requirement file
COPY ./requirements.txt ./

# Upgrading pip version
RUN pip install --upgrade pip

# Installing dependencies
RUN pip install gunicorn

# Installing dependencies
RUN pip install -r ./requirements.txt

# Copying all the files in our project
COPY . .
