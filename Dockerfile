FROM python:3.9.17-slim-bullseye

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "role_menu.py"]