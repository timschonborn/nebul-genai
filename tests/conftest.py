import pytest
from nebul_genai.types import Document, Chunk


@pytest.fixture
def sample_document():
    return Document(
        content="This is a test document.",
        metadata={"source": "test"},
        source="test.txt",
    )


@pytest.fixture
def sample_chunk():
    return Chunk(
        content="This is a test chunk.",
        document_id="test-doc",
        chunk_index=0,
        metadata={"position": "first"},
    )
