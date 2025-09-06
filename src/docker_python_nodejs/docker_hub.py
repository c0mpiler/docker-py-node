from typing import TypedDict

import requests


class DockerImageDict(TypedDict):
    architecture: str
    features: str
    variant: str | None
    digest: str
    os: str
    os_features: str
    os_version: str | None
    size: int
    status: str
    last_pulled: str
    last_pushed: str


class DockerTagDict(TypedDict):
    creator: int
    id: int
    images: list[DockerImageDict]
    last_updated: str
    last_updater: int
    last_updater_username: str
    name: str
    repository: int
    full_size: int
    v2: bool
    tag_status: str
    tag_last_pulled: str
    tag_last_pushed: str
    media_type: str
    content_type: str
    digest: str


class DockerTagResponse(TypedDict):
    count: int
    next: str | None
    previous: str | None
    results: list[DockerTagDict]


def fetch_tags(package: str, page: int = 1, max_retries: int = 3) -> list[DockerTagDict]:
    """Fetch available docker tags.

    Iterates over paginated responses from the Docker Hub API collecting all
    tags. If a request fails it is retried ``max_retries`` times before raising
    a ``RuntimeError`` with context information.
    """

    tags: list[DockerTagDict] = []
    next_page: str | None = "start"

    while next_page:
        for attempt in range(1, max_retries + 1):
            try:
                result = requests.get(
                    f"https://registry.hub.docker.com/v2/namespaces/library/repositories/{package}/tags",
                    params={"page": page, "page_size": 100},
                    timeout=10.0,
                )
                result.raise_for_status()
            except requests.RequestException as exc:  # pragma: no cover - exercised via tests
                if attempt == max_retries:
                    raise RuntimeError(
                        f"Failed to fetch tags for {package} after {max_retries} attempts (page {page})"
                    ) from exc
            else:
                data: DockerTagResponse = result.json()
                tags.extend(data["results"])
                next_page = data["next"]
                page += 1
                break

    return tags
