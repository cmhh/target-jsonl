"""JSONL target class."""

from __future__ import annotations

from singer_sdk import typing as th
from singer_sdk.target_base import Target

from target_jsonl.sinks import (
    JSONLSink,
)

class TargetJSONL(Target):
    """Sample target for JSONL."""

    name = "target-jsonl"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "filepath",
            th.StringType,
            description="The path to the target output file",
        ),
    ).to_dict()

    default_sink_class = JSONLSink

if __name__ == "__main__":
    TargetJSONL.cli()
