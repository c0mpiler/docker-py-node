import pytest
import responses

from docker_python_nodejs.docker_hub import fetch_tags
from docker_python_nodejs.nodejs_versions import (
    fetch_node_releases,
    fetch_node_unofficial_releases,
    fetch_nodejs_release_schedule,
)
from docker_python_nodejs.versions import scrape_supported_python_versions


@responses.activate
@pytest.mark.parametrize(
    ("func", "url", "payload"),
    [
        (
            fetch_node_releases,
            "https://nodejs.org/dist/index.json",
            [{"version": "v1.0.0", "date": "2000-01-01", "files": []}],
        ),
        (
            fetch_node_unofficial_releases,
            "https://unofficial-builds.nodejs.org/download/release/index.json",
            [{"version": "v1.0.0", "date": "2000-01-01", "files": []}],
        ),
    ],
)
def test_node_release_fetchers_retry(func, url, payload) -> None:
    responses.add(responses.GET, url, status=500)
    responses.add(responses.GET, url, json=payload, status=200)
    assert func() == payload
    assert len(responses.calls) == 2


@responses.activate
def test_fetch_nodejs_release_schedule_retry() -> None:
    url = "https://raw.githubusercontent.com/nodejs/Release/master/schedule.json"
    data = {
        "v1": {
            "start": "2000-01-01",
            "lts": "2000-06-01",
            "maintenance": "2000-07-01",
            "end": "2100-01-01",
            "codename": "foo",
        }
    }
    responses.add(responses.GET, url, status=500)
    responses.add(responses.GET, url, json=data, status=200)
    assert fetch_nodejs_release_schedule() == data
    assert len(responses.calls) == 2


@responses.activate
def test_fetch_tags_retry() -> None:
    url = "https://registry.hub.docker.com/v2/namespaces/library/repositories/python/tags?page=1&page_size=100"
    result = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{"name": "3.11.4-bookworm", "images": []}],
    }
    responses.add(responses.GET, url, status=500)
    responses.add(responses.GET, url, json=result, status=200)
    assert fetch_tags("python") == result["results"]
    assert len(responses.calls) == 2


@responses.activate
def test_scrape_supported_python_versions_retry() -> None:
    url = "https://devguide.python.org/versions/"
    html = """
    <table id='supported-versions'>
      <tbody>
        <tr>
          <td>3.11</td><td></td><td></td>
          <td>2000-01-01</td><td>2100-01-01</td><td></td>
        </tr>
      </tbody>
    </table>
    """
    responses.add(responses.GET, url, status=500)
    responses.add(responses.GET, url, body=html, status=200)
    versions = scrape_supported_python_versions()
    assert len(versions) == 1
    assert versions[0].version == "3.11"
    assert len(responses.calls) == 2
