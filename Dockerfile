FROM ubuntu:latest as base
RUN mkdir family_account
COPY pyproject.toml /family_account/pyproject.toml

FROM python:3.9 as py
COPY --from=base /family_account /family_account
WORKDIR /family_account
RUN --mount=type=cache,target=/root/.cache/pip pip install poetry
RUN poetry config virtualenvs.create false
RUN mkdir .poetry_cache
RUN poetry config cache-dir /family_account/.poetry_cache
RUN --mount=type=cache,target=/family_account/.poetry_cache poetry install

FROM py as source
WORKDIR /family_account

CMD pytest -s tests/run
