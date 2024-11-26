from ..types.document import Document


class BaseLoader:
    def load(self, file_path: str) -> Document:
        pass
