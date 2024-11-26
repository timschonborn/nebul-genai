from typing import List

from ..base.base_chunker import BaseChunker
from ..types.chunk import Chunk


class HeaderChunker(BaseChunker):
    def __init__(self, chunk_size: int, chunk_overlap: int):
        super().__init__(chunk_size, chunk_overlap)

    def chunk(self, text: str) -> List[Chunk]:
        pass
