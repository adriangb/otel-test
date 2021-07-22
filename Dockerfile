FROM python:3.9-slim as base
RUN mkdir /project
WORKDIR /project
COPY . .
RUN apt-get update && apt-get install -y make
RUN make init
CMD make run-app
