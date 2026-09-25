from click.testing import CliRunner

from captrain import __version__
from captrain.cli.main import main


def test_version_option() -> None:
    result = CliRunner().invoke(main, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_help_shows_groups() -> None:
    result = CliRunner().invoke(main, ["--help"])
    assert result.exit_code == 0
    for group in ("data", "dataset", "experiment", "model", "infer", "pipeline"):
        assert group in result.output


def test_data_inspect_stub() -> None:
    result = CliRunner().invoke(main, ["data", "inspect", "data/dataset.csv"])
    assert result.exit_code == 0
    assert "not_implemented" in result.output


def test_data_validate_stub() -> None:
    result = CliRunner().invoke(main, ["data", "validate", "data/dataset.csv"])
    assert result.exit_code == 0
    assert "not_implemented" in result.output


def test_dataset_prepare_stub() -> None:
    result = CliRunner().invoke(main, ["dataset", "prepare", "data/dataset.csv"])
    assert result.exit_code == 0
    assert "not_implemented" in result.output


def test_json_output_is_parseable() -> None:
    import json

    result = CliRunner().invoke(main, ["--json", "data", "inspect", "data/dataset.csv"])
    assert result.exit_code == 0
    payload = json.loads(result.output)
    assert payload["tool"] == "inspect_dataset"
    assert payload["status"] == "not_implemented"
