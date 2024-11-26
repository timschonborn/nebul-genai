from PyPDF2 import PdfReader

from ..base.base_loader import BaseLoader
from ..types.document import Document


class PyPDF2Loader(BaseLoader):
    def load(self, file_path: str, sep=" ") -> Document:
        if file_path.endswith(".pdf"):
            reader = PdfReader(file_path)
            content = sep.join([page.extract_text() for page in reader.pages])
        else:
            raise ValueError(f"Unsupported file type: {file_path}")
        return Document(content=content)
