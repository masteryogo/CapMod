"""CapTrain CLI — the human interface over the core toolkit.

Every command is a thin wrapper that ultimately delegates to the core.
A global ``--json`` flag produces structured (JSON) output for AI agents.
"""

from __future__ import annotations

import json
from typing import Any

import click

from captrain.core.data.inspect import inspect_dataset
from captrain.core.data.prepare import prepare_dataset
from captrain.core.data.validate import validate_dataset


@click.group()
@click.option(
    "--json",
    "as_json",
    is_flag=True,
    help="Emit structured JSON output (agent-friendly).",
)
@click.version_option(package_name="captrain", prog_name="cap")
@click.pass_context
def main(ctx: click.Context, as_json: bool) -> None:
    """CapTrain — one ML engineering layer for humans and agents."""
    ctx.ensure_object(dict)
    ctx.obj["json"] = as_json


def emit(ctx: click.Context, payload: dict[str, Any]) -> None:
    """Render a core result as JSON (when ``--json``) or rich text."""
    if ctx.obj["json"]:
        click.echo(json.dumps(payload, indent=2, default=str))
        return
    click.echo(payload.get("status", ""))
    for key, value in payload.items():
        click.echo(f"{key}: {value}")


@main.group("data")
def data_group() -> None:
    """Data inspection and validation."""


@data_group.command("inspect")
@click.argument("dataset_path")
@click.pass_context
def data_inspect(ctx: click.Context, dataset_path: str) -> None:
    """Inspect a dataset (schema, metrics, anomalies)."""
    emit(ctx, inspect_dataset(dataset_path))


@data_group.command("validate")
@click.argument("dataset_path")
@click.pass_context
def data_validate(ctx: click.Context, dataset_path: str) -> None:
    """Validate a dataset against quality rules."""
    emit(ctx, validate_dataset(dataset_path))


@main.group("dataset")
def dataset_group() -> None:
    """Dataset preparation."""


@dataset_group.command("prepare")
@click.argument("dataset_path")
@click.pass_context
def dataset_prepare(ctx: click.Context, dataset_path: str) -> None:
    """Prepare a dataset for training."""
    emit(ctx, prepare_dataset(dataset_path))


@main.group("experiment")
def experiment_group() -> None:
    """Experiment tracking and comparison."""


@experiment_group.command("compare")
@click.pass_context
def experiment_compare(ctx: click.Context) -> None:
    """Compare experiments (not implemented yet)."""
    emit(ctx, {"tool": "compare_experiments", "status": "not_implemented"})


@main.group("model")
def model_group() -> None:
    """Model registry."""


@model_group.command("register")
@click.pass_context
def model_register(ctx: click.Context) -> None:
    """Register a model version (not implemented yet)."""
    emit(ctx, {"tool": "register_model", "status": "not_implemented"})


@main.command("train")
@click.pass_context
def train(ctx: click.Context) -> None:
    """Train a model (not implemented yet)."""
    emit(ctx, {"tool": "train_model", "status": "not_implemented"})


@main.command("eval")
@click.pass_context
def eval_command(ctx: click.Context) -> None:
    """Evaluate a model (not implemented yet)."""
    emit(ctx, {"tool": "evaluate_model", "status": "not_implemented"})


@main.command("benchmark")
@click.pass_context
def benchmark(ctx: click.Context) -> None:
    """Benchmark model performance (not implemented yet)."""
    emit(ctx, {"tool": "benchmark", "status": "not_implemented"})


@main.command("predict")
@click.pass_context
def predict(ctx: click.Context) -> None:
    """Batch inference (not implemented yet)."""
    emit(ctx, {"tool": "predict", "status": "not_implemented"})


@main.group("infer")
def infer_group() -> None:
    """Inference serving."""


@infer_group.command("serve")
@click.pass_context
def infer_serve(ctx: click.Context) -> None:
    """Serve a model (not implemented yet)."""
    emit(ctx, {"tool": "serve", "status": "not_implemented"})


@main.group("pipeline")
def pipeline_group() -> None:
    """Pipeline orchestration."""


@pipeline_group.command("run")
@click.option("--config", type=click.Path(exists=True), help="Pipeline config file.")
@click.pass_context
def pipeline_run(ctx: click.Context, config: str | None) -> None:
    """Run an end-to-end pipeline (not implemented yet)."""
    emit(ctx, {"tool": "run_pipeline", "status": "not_implemented", "config": config})


__all__: list[str] = ["main"]
