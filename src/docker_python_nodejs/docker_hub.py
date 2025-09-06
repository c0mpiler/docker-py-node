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


def fetch_tags(package: str, page: int = 1, name: str | None = None) -> list[DockerTagDict]:
    """Fetch available docker tags.

    The Docker Hub API supports a ``name`` query parameter that performs a
    substring match on tag names.  By passing a value for ``name`` we can limit
    the result set to tags that contain that value, which avoids enumerating the
    entire tag collection for a repository.
    """

    params = {"page": page, "page_size": 100}
    if name:
        params["name"] = name

    result = requests.get(
        f"https://registry.hub.docker.com/v2/namespaces/library/repositories/{package}/tags",
        params=params,
        timeout=10.0,
    )
    result.raise_for_status()
    data: DockerTagResponse = result.json()
    if not data["next"]:
        return data["results"]
    return data["results"] + fetch_tags(package, page=page + 1, name=name)
