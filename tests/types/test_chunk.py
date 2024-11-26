from nebul_genai.types import Chunk


def test_chunk_creation():
    chunk = Chunk(
        content="Test content", start_index=0, end_index=10, metadata={"position": 0}
    )
    assert chunk.content == "Test content"
    assert chunk.start_index == 0
    assert chunk.end_index == 10
    assert chunk.metadata["position"] == 0


def test_chunk_with_fixture(sample_chunk):
    assert isinstance(sample_chunk, Chunk)
    assert sample_chunk.content == "This is the first test chunk."
    assert sample_chunk.start_index == 0
    assert sample_chunk.end_index == 10
    assert sample_chunk.metadata["position"] == 0


def test_chunk_optional_fields():
    chunk = Chunk(content="Test content")
    assert chunk.content == "Test content"
    assert chunk.start_index is None
    assert chunk.end_index is None
    assert chunk.metadata is None


def test_multiple_chunks(sample_chunk, sample_chunk_2):
    assert sample_chunk.content != sample_chunk_2.content
    assert sample_chunk.metadata["position"] == 0
    assert sample_chunk_2.metadata["position"] == 1
    assert sample_chunk.end_index + 1 == sample_chunk_2.start_index
