# Generated {{ now }}
# python: {{ python_canonical }}
# nodejs: {{ nodejs_canonical }}
FROM python:{{ python_image }}
LABEL org.opencontainers.image.authors="c0mpiler <c0mpiler@ins8s.dev>"

RUN groupadd --gid 1000 c0mpiler && useradd --uid 1000 --gid c0mpiler --shell /bin/bash --create-home c0mpiler
ENV POETRY_HOME=/usr/local

RUN \
{% if distro_variant == "slim" %}  apt-get update && apt-get install curl gnupg2 xz-utils -yqq && \
{% endif %}  apt-get upgrade -yqq && \
  rm -rf /var/lib/apt/lists/*
RUN NODE_VERSION="v{{ nodejs_canonical }}" \
  ARCH= && dpkgArch="$(dpkg --print-architecture)" \
  && case "${dpkgArch##*-}" in \
    amd64) ARCH='x64';; \
    arm64) ARCH='arm64';; \
    *) echo "unsupported architecture"; exit 1 ;; \
  esac \
  && for key in $(curl -sL https://raw.githubusercontent.com/nodejs/docker-node/HEAD/keys/node.keys); do \
    gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys "$key" || \
    gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "$key" ; \
  done \
  && curl -fsSLO --compressed "https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-linux-$ARCH.tar.xz" \
  && curl -fsSLO --compressed "https://nodejs.org/dist/$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
  && rm "node-$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs
RUN corepack enable yarn

RUN pip install -U pip pipenv uv && \
  curl -fsSL --compressed https://install.python-poetry.org | python -
