FROM python:3.9.17-slim-bullseye

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# CMD ["python3", "role_menu.py"]
CMD ["docker-compose", "run", "my_image", "python", "shell"]
# docker-compose run my_image python role_menu.py shell