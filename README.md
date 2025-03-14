# 🐳 Python with Node.js Docker Images

[![Docker Hub](https://img.shields.io/docker/pulls/c0mpiler/python-nodejs.svg?cache=none&style=flat-square&logo=docker&label=Docker%20Hub)](https://hub.docker.com/r/c0mpiler/python-nodejs/)
[![GitHub Container Registry](https://img.shields.io/badge/GHCR-image-2088FF?style=flat-square&logo=github)](https://github.com/c0mpiler/docker-py-node/pkgs/container/python-nodejs)
[![Docker Repository on Quay](https://quay.io/repository/c0mpiler/python-nodejs/status "Docker Repository on Quay")](https://quay.io/repository/c0mpiler/python-nodejs)
[![CI/CD Status](https://img.shields.io/github/actions/workflow/status/c0mpiler/docker-py-node/build.yaml?style=flat-square&label=CI%2FCD)](https://github.com/c0mpiler/docker-py-node/actions)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)

Production-ready Docker images featuring Python and Node.js in various combinations. Perfect for projects requiring both ecosystems.

Available on [Docker Hub](https://hub.docker.com/r/c0mpiler/python-nodejs/), [GitHub Container Registry](https://github.com/c0mpiler/docker-py-node/pkgs/container/python-nodejs), and [Quay.io](https://quay.io/repository/c0mpiler/python-nodejs).

Last updated: 2025-03-11

## Features

- **Multiple version combinations**: All supported Python and Node.js versions
- **Multiple distributions**: Debian Bookworm (default), Bullseye, Slim, and Alpine
- **Multi-registry availability**: Available on Docker Hub, GitHub Container Registry, and Quay.io
- **Multi-architecture support**: linux/amd64 and linux/arm64 (except Alpine: amd64 only)
- **Thoroughly tested**: Each image undergoes comprehensive testing
- **Regularly updated**: Automatic updates via GitHub Actions
- **User-friendly**: Default non-root user (`c0mpiler`) preconfigured

## Latest Image Details

The `latest` tag currently includes:

| Component | Version |
|-----------|---------|
| Python    | latest  |
| Node.js   | 22.x    |
| npm       | 10.x    |
| yarn      | stable  |
| pip       | latest  |
| pipenv    | latest  |
| poetry    | latest  |
| uv        | latest  |

## Available Tags

Select the specific combination of Python and Node.js versions that suits your needs:

<!-- TAGS_START -->

Tag | Python version | Node.js version | Distro
--- | --- | --- | ---
`python3.13-nodejs23` | 3.13.2 | 23.10.0 | bookworm
`python3.13-nodejs23-bullseye` | 3.13.2 | 23.10.0 | bullseye
`python3.13-nodejs23-slim` | 3.13.2 | 23.10.0 | slim
`python3.13-nodejs23-alpine` | 3.13.2 | 23.10.0 | alpine
`python3.13-nodejs22` | 3.13.2 | 22.14.0 | bookworm
`python3.13-nodejs22-bullseye` | 3.13.2 | 22.14.0 | bullseye
`python3.13-nodejs22-slim` | 3.13.2 | 22.14.0 | slim
`python3.13-nodejs22-alpine` | 3.13.2 | 22.14.0 | alpine
`python3.13-nodejs20` | 3.13.2 | 20.19.0 | bookworm
`python3.13-nodejs20-bullseye` | 3.13.2 | 20.19.0 | bullseye
`python3.13-nodejs20-slim` | 3.13.2 | 20.19.0 | slim
`python3.13-nodejs20-alpine` | 3.13.2 | 20.19.0 | alpine
`python3.13-nodejs18` | 3.13.2 | 18.20.7 | bookworm
`python3.13-nodejs18-bullseye` | 3.13.2 | 18.20.7 | bullseye
`python3.13-nodejs18-slim` | 3.13.2 | 18.20.7 | slim
`python3.13-nodejs18-alpine` | 3.13.2 | 18.20.7 | alpine
`python3.12-nodejs23` | 3.12.9 | 23.10.0 | bookworm
`python3.12-nodejs23-bullseye` | 3.12.9 | 23.10.0 | bullseye
`python3.12-nodejs23-slim` | 3.12.9 | 23.10.0 | slim
`python3.12-nodejs23-alpine` | 3.12.9 | 23.10.0 | alpine
`python3.12-nodejs22` | 3.12.9 | 22.14.0 | bookworm
`python3.12-nodejs22-bullseye` | 3.12.9 | 22.14.0 | bullseye
`python3.12-nodejs22-slim` | 3.12.9 | 22.14.0 | slim
`python3.12-nodejs22-alpine` | 3.12.9 | 22.14.0 | alpine
`python3.12-nodejs20` | 3.12.9 | 20.19.0 | bookworm
`python3.12-nodejs20-bullseye` | 3.12.9 | 20.19.0 | bullseye
`python3.12-nodejs20-slim` | 3.12.9 | 20.19.0 | slim
`python3.12-nodejs20-alpine` | 3.12.9 | 20.19.0 | alpine
`python3.12-nodejs18` | 3.12.9 | 18.20.7 | bookworm
`python3.12-nodejs18-bullseye` | 3.12.9 | 18.20.7 | bullseye
`python3.12-nodejs18-slim` | 3.12.9 | 18.20.7 | slim
`python3.12-nodejs18-alpine` | 3.12.9 | 18.20.7 | alpine
`python3.11-nodejs23` | 3.11.11 | 23.10.0 | bookworm
`python3.11-nodejs23-bullseye` | 3.11.11 | 23.10.0 | bullseye
`python3.11-nodejs23-slim` | 3.11.11 | 23.10.0 | slim
`python3.11-nodejs23-alpine` | 3.11.11 | 23.10.0 | alpine
`python3.11-nodejs22` | 3.11.11 | 22.14.0 | bookworm
`python3.11-nodejs22-bullseye` | 3.11.11 | 22.14.0 | bullseye
`python3.11-nodejs22-slim` | 3.11.11 | 22.14.0 | slim
`python3.11-nodejs22-alpine` | 3.11.11 | 22.14.0 | alpine
`python3.11-nodejs20` | 3.11.11 | 20.19.0 | bookworm
`python3.11-nodejs20-bullseye` | 3.11.11 | 20.19.0 | bullseye
`python3.11-nodejs20-slim` | 3.11.11 | 20.19.0 | slim
`python3.11-nodejs20-alpine` | 3.11.11 | 20.19.0 | alpine
`python3.11-nodejs18` | 3.11.11 | 18.20.7 | bookworm
`python3.11-nodejs18-bullseye` | 3.11.11 | 18.20.7 | bullseye
`python3.11-nodejs18-slim` | 3.11.11 | 18.20.7 | slim
`python3.11-nodejs18-alpine` | 3.11.11 | 18.20.7 | alpine
`python3.10-nodejs23` | 3.10.16 | 23.10.0 | bookworm
`python3.10-nodejs23-bullseye` | 3.10.16 | 23.10.0 | bullseye
`python3.10-nodejs23-slim` | 3.10.16 | 23.10.0 | slim
`python3.10-nodejs23-alpine` | 3.10.16 | 23.10.0 | alpine
`python3.10-nodejs22` | 3.10.16 | 22.14.0 | bookworm
`python3.10-nodejs22-bullseye` | 3.10.16 | 22.14.0 | bullseye
`python3.10-nodejs22-slim` | 3.10.16 | 22.14.0 | slim
`python3.10-nodejs22-alpine` | 3.10.16 | 22.14.0 | alpine
`python3.10-nodejs20` | 3.10.16 | 20.19.0 | bookworm
`python3.10-nodejs20-bullseye` | 3.10.16 | 20.19.0 | bullseye
`python3.10-nodejs20-slim` | 3.10.16 | 20.19.0 | slim
`python3.10-nodejs20-alpine` | 3.10.16 | 20.19.0 | alpine
`python3.10-nodejs18` | 3.10.16 | 18.20.7 | bookworm
`python3.10-nodejs18-bullseye` | 3.10.16 | 18.20.7 | bullseye
`python3.10-nodejs18-slim` | 3.10.16 | 18.20.7 | slim
`python3.10-nodejs18-alpine` | 3.10.16 | 18.20.7 | alpine
`python3.9-nodejs23` | 3.9.21 | 23.10.0 | bookworm
`python3.9-nodejs23-bullseye` | 3.9.21 | 23.10.0 | bullseye
`python3.9-nodejs23-slim` | 3.9.21 | 23.10.0 | slim
`python3.9-nodejs23-alpine` | 3.9.21 | 23.10.0 | alpine
`python3.9-nodejs22` | 3.9.21 | 22.14.0 | bookworm
`python3.9-nodejs22-bullseye` | 3.9.21 | 22.14.0 | bullseye
`python3.9-nodejs22-slim` | 3.9.21 | 22.14.0 | slim
`python3.9-nodejs22-alpine` | 3.9.21 | 22.14.0 | alpine
`python3.9-nodejs20` | 3.9.21 | 20.19.0 | bookworm
`python3.9-nodejs20-bullseye` | 3.9.21 | 20.19.0 | bullseye
`python3.9-nodejs20-slim` | 3.9.21 | 20.19.0 | slim
`python3.9-nodejs20-alpine` | 3.9.21 | 20.19.0 | alpine
`python3.9-nodejs18` | 3.9.21 | 18.20.7 | bookworm
`python3.9-nodejs18-bullseye` | 3.9.21 | 18.20.7 | bullseye
`python3.9-nodejs18-slim` | 3.9.21 | 18.20.7 | slim
`python3.9-nodejs18-alpine` | 3.9.21 | 18.20.7 | alpine

<!-- TAGS_END -->

These tags are automatically updated when new minor or patch versions are released. The update process runs twice daily via [GitHub Actions](https://github.com/c0mpiler/docker-py-node/actions).

## Supported Version Lifecycles

<!-- SUPPORTED_VERSIONS_START -->

Python version | Start | End
--- | --- | ---
3.13 | 2024-10-07 | 2029-10
3.12 | 2023-10-02 | 2028-10
3.11 | 2022-10-24 | 2027-10
3.10 | 2021-10-04 | 2026-10
3.9 | 2020-10-05 | 2025-10

Node.js version | Start | End
--- | --- | ---
v23 | 2024-10-16 | 2025-06-01
v22 | 2024-04-24 | 2027-04-30
v20 | 2023-04-18 | 2026-04-30
v18 | 2022-04-19 | 2025-04-30

<!-- SUPPORTED_VERSIONS_END -->

Version information is updated automatically from official sources:
- Python: [devguide.python.org/versions](https://devguide.python.org/versions/#supported-versions)
- Node.js: [github.com/nodejs/Release](https://github.com/nodejs/Release/blob/main/schedule.json)

## Usage

### Basic Usage

```bash
# Pull from Docker Hub
docker pull c0mpiler/python-nodejs:latest

# Pull from GitHub Container Registry
docker pull ghcr.io/c0mpiler/python-nodejs:latest

# Pull from Quay.io
docker pull quay.io/c0mpiler/python-nodejs:latest

# Run interactive shell
docker run -it c0mpiler/python-nodejs bash

# Build from GitHub
docker build -t c0mpiler/python-nodejs github.com/c0mpiler/docker-py-node
```

### Using as a Base Image

```dockerfile
# Using Docker Hub
FROM c0mpiler/python-nodejs:python3.12-nodejs22

# OR using GitHub Container Registry
# FROM ghcr.io/c0mpiler/python-nodejs:python3.12-nodejs22

# OR using Quay.io
# FROM quay.io/c0mpiler/python-nodejs:python3.12-nodejs22

# Use the pre-configured non-root user
USER c0mpiler
WORKDIR /home/c0mpiler/app

# Add your application code
COPY --chown=c0mpiler:c0mpiler . .

# Install dependencies
RUN pip install -r requirements.txt && \
    npm install

# Run your application
CMD ["python", "app.py"]
```

All images include a non-root user `c0mpiler` with uid 1000 and gid 1000, suitable for most development and production environments.

## Container Registry Options

These images are available on multiple registries to ensure high availability and flexibility:

| Registry | URL | Pull Command Example |
|----------|-----|----------------------|
| Docker Hub | [c0mpiler/python-nodejs](https://hub.docker.com/r/c0mpiler/python-nodejs/) | `docker pull c0mpiler/python-nodejs:latest` |
| GitHub Container Registry | [ghcr.io/c0mpiler/python-nodejs](https://github.com/c0mpiler/python-nodejs/pkgs/container/python-nodejs) | `docker pull ghcr.io/c0mpiler/python-nodejs:latest` |
| Quay.io | [quay.io/c0mpiler/python-nodejs](https://quay.io/repository/c0mpiler/python-nodejs) | `docker pull quay.io/c0mpiler/python-nodejs:latest` |

All registries are automatically updated with each release. You can use the registry that best fits your infrastructure or requirements.

## For Maintainers

This repository contains tools for generating and maintaining the Docker images:

```bash
# Install project dependencies
pip install -e .

# View available commands
ninja --help

# Generate a specific Dockerfile
ninja generate-dockerfile --python-version 3.12 --nodejs-version 18 --distro bookworm

# Update version information
ninja update-versions

# Display currently supported versions
ninja show-versions
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
