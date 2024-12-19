FROM python:alpine

COPY . .

RUN pip install poetry

RUN poetry shell

RUN poetry install

CMD ["python", "main.py"]
