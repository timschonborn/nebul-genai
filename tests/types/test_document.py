from nebul_genai.types import Document


def test_document_creation():
    doc = Document(content="Test content", chunks=[], metadata={"source": "test"})
    assert doc.content == "Test content"
    assert doc.chunks == "test.txt"
    assert doc.metadata["source"] == "test"


def test_document_with_fixture(sample_document):
    assert isinstance(sample_document, Document)
    assert sample_document.content == "This is a test document."
