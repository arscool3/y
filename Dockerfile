FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

WORKDIR /src

RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install

CMD streamlit run main.py --server.headless=true --server.port=8000