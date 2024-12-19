FROM python:alpine

COPY . .

RUN pip install poetry

RUN poetry install

CMD ["poetry", "run", "python", "main.py"]
