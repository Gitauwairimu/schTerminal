#Dockerfile
FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir /application
WORKDIR "/application"
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*ADD requirements.txt /application/
COPY . .
# ADD src/script.py /application/
RUN pip install -r /application/requirements.txt
CMD [ "python3", "role_menu.py" ]
