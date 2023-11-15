FROM python:3.11.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /service
COPY ./pyproject.toml ./poetry.lock /service/app/
COPY ./ /service/app/
#COPY ./server/pyproject.toml ./server/poetry.lock /service/app/
#COPY ./server/ /service/app/
WORKDIR /service/app

RUN python -m pip install --upgrade pip
RUN python -m pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi
#
#EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
