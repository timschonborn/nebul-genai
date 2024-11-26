from dataclasses import dataclass
from typing import Optional


@dataclass
class Chunk:
    """Represents a chunk of text with optional metadata."""

    content: str
    start_index: Optional[int] = None
    end_index: Optional[int] = None
    metadata: Optional[dict] = None
