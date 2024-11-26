import pytest
from nebul_genai.types import Document, Chunk


@pytest.fixture
def sample_document():
    return Document(
        content="This is a test document.",
        chunks=[],
        metadata={"source": "test.pdf"},
    )


@pytest.fixture
def sample_document_with_chunk():
    return Document(
        content="This is a test document.",
        chunks=[sample_chunk()],
        metadata={"source": "test.pdf"},
    )


@pytest.fixture
def sample_document_with_two_chunks():
    return Document(
        content="This is a test document.",
        chunks=[sample_chunk(), sample_chunk_2()],
        metadata={"source": "test.pdf"},
    )


@pytest.fixture
def sample_chunk():
    return Chunk(
        content="This is the first test chunk.",
        start_index=0,
        end_index=10,
        metadata={"position": 0},
    )


@pytest.fixture
def sample_chunk_2():
    return Chunk(
        content="This is the second test chunk.",
        start_index=11,
        end_index=20,
        metadata={"position": 1},
    )
