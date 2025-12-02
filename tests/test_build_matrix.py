from pathlib import Path

import pytest
from docker_python_nodejs import build_matrix


def test_github_action_set_output_splits_newlines(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    output_file = tmp_path / "out.txt"
    monkeypatch.setattr(build_matrix, "GITHUB_OUTPUT", str(output_file))

    build_matrix._github_action_set_output("FIRST", "1")
    build_matrix._github_action_set_output("SECOND", "2")

    lines = output_file.read_text().splitlines()
    assert lines == ["FIRST=1", "SECOND=2"]
