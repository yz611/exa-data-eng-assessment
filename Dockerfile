# set base image (host OS)
FROM python:3.8

# copy the content of the local src directory to the working directory
COPY ./ /exa-data-eng-assessment

# install dependencies
RUN ls -la /exa-data-eng-assessment/*

# set the working directory in the container
WORKDIR /exa-data-eng-assessment/scripts

# command to run on container start
CMD [ "python", "./testing.py" ]