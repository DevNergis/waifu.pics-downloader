FROM python:alpine

COPY . .

RUN apk add bash

RUN bash

RUN pip install poetry

RUN poetry shell

RUN poetry install

CMD ["python", "main.py"]
