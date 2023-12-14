#Dockerfile
FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir /application
WORKDIR "/application"# Upgrade pip
RUN pip install --upgrade pip# Update
RUN apt-get update \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*ADD requirements.txt /application/
COPY . .
# ADD src/script.py /application/
RUN pip install -r /application/requirements.txt
CMD [ "python", "role_menu.py" ]
