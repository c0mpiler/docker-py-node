# Generated {{ now }}
# python: {{ python_canonical }}
# nodejs: {{ nodejs_canonical }}
FROM python:{{ python_image }} as builder

# Install node prereqs, nodejs and yarn
# Ref: https://raw.githubusercontent.com/nodejs/docker-node/master/Dockerfile-alpine.template
# Ref: https://yarnpkg.com/en/docs/install
{% if python == "3.7" or python == "3.8" %}
# poetry: Workaround for missing cffi musllinux wheels on olds pythons. Ref: https://foss.heptapod.net/pypy/cffi/-/issues/509
RUN apk add gcc musl-dev libffi-dev
RUN pip install cffi
RUN find /root/.cache/pip/wheels -name '*.whl' -exec cp {} / +
{% endif %}
RUN apk add curl
# FIXME: no arm + musl build yet
# Ref: https://github.com/nodejs/unofficial-builds/pull/59
# Ref: https://github.com/nodejs/node/pull/45756
RUN curl -fsSLO --compressed "https://unofficial-builds.nodejs.org/download/release/v{{ nodejs_canonical }}/node-v{{ nodejs_canonical }}-linux-x64-musl.tar.xz"
RUN curl -fsSLO --compressed "https://unofficial-builds.nodejs.org/download/release/v{{ nodejs_canonical }}/SHASUMS256.txt"
RUN grep " node-v{{ nodejs_canonical }}-linux-x64-musl.tar.xz\$" SHASUMS256.txt | sha256sum -c -
RUN tar -xf "node-v{{ nodejs_canonical }}-linux-x64-musl.tar.xz"

FROM python:{{ python_image }}
LABEL org.opencontainers.image.authors="c0mpiler <c0mpiler@ins8s.dev>"

RUN addgroup -g 1000 c0mpiler && adduser -u 1000 -G c0mpiler -s /bin/sh -D c0mpiler
RUN apk add libstdc++
COPY --from=builder /node-v{{ nodejs_canonical }}-linux-x64-musl /usr/local
RUN corepack enable yarn
RUN pip install -U pip pipenv uv

# Poetry
# Mimic what https://install.python-poetry.org does without the flexibility (platforms, install sources, etc).
ENV VENV=/opt/poetryvenv
RUN python -m venv $VENV && $VENV/bin/pip install -U pip wheel
{% if python == "3.7" or python == "3.8" %}
# Workaround for missing cffi musllinux wheels on older pythons
COPY --from=builder /*.whl /
RUN $VENV/bin/pip install /*.whl && rm /*.whl
{% endif %}
RUN $VENV/bin/pip install poetry && ln -s $VENV/bin/poetry /usr/local/bin/poetry
