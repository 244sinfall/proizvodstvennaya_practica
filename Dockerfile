FROM python:3.12.2-slim-bookworm

ENV PATH="/home/app/.local/bin:${PATH}"

WORKDIR /app
RUN mkdir /data && \
    useradd -ms /bin/bash app && \
    chown app:app /data/

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install

USER app

COPY ./src .

CMD ["/bin/bash"]
