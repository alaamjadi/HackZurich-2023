from pathlib import Path
from typing import Union

from docx import Document


class DocxHandler:
    def __call__(self, path: Union[str, Path]) -> bool:
        document = Document(path)
        head = document.paragraphs[0].text
        if head == "Financial Analysis Report":
            return False
        elif len(head.split(" ")) == 2:
            return True
