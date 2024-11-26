import pytest
from nebul_genai.types import Document, Chunk


@pytest.fixture
def sample_document():
    return Document(
        content="This is a test document.",
        chunks=[],
        metadata={"source": "test"},
    )


@pytest.fixture
def sample_chunk():
    return Chunk(
        content="This is a test chunk.",
        start_index=0,
        end_index=10,
        metadata={"position": "first"},
    )
