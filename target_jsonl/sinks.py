"""JSONL target sink class, which handles writing streams."""

from __future__ import annotations
from singer_sdk.sinks import BatchSink
import json

class JSONLSink(BatchSink):
    """JSONL target sink class."""

    max_size = 10000  

    def process_batch(self, context: dict) -> None:
        """Write out any prepped records and return once fully written.

        Args:
            context: Stream partition or context dictionary.
        """
        with open(self.config.get("filepath"), 'at') as f:
            for record in context['records']:
                entry = json.dumps(record) + "\n"
                f.write(str)

