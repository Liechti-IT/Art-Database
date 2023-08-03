# base image  
FROM python:3.11

# setup environment variable  
ENV DockerHOME=/app

# set work directory  
RUN mkdir -p $DockerHOME

RUN mkdir $DockerHOME/static
RUN mkdir $DockerHOME/media
RUN mkdir $DockerHOME/db

# where your code lives  
WORKDIR $DockerHOME

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies  
RUN pip install --upgrade pip

# copy whole project to your docker home directory. 
COPY . $DockerHOME

# run this command to install all dependencies  
RUN pip install -r requirements.txt

RUN addgroup --system app && adduser --system --group app

# chown all the files to the app user
RUN chown -R app:app $DockerHOME

# change to the app user
USER app