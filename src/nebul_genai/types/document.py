from dataclasses import dataclass
from typing import List, Optional

from .chunk import Chunk


@dataclass
class Document:
    """Represents a document with its content and optional metadata."""

    content: str
    chunks: Optional[List[Chunk]] = None
    metadata: Optional[dict] = None
