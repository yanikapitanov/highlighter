"""Something to parse"""
from typing import List, Union

from fastapi import UploadFile

from app.model.models import Highlight


class Parser:
    """Parse me baby one more time"""

    def __init__(self, file: UploadFile):
        self.file = file

    def parse(self) -> List[Highlight]:
        """Something wicked this way comes"""
        highlights = self.file.file.read().decode("utf-8").replace("\r\n", "\n").lstrip("\ufeff").split("==========")
        return [Parser.map_highlight(highlight) for highlight in highlights]

    @staticmethod
    def map_highlight(chunk: str) -> Union[Highlight, None]:
        line = [line for line in chunk.split("\n") if line != ""]
        if len(line) < 3:
            return None
        split_index = line[0].rfind("(")
        author = line[0][split_index:].replace(")", "").replace("(", "").strip()
        title = line[0][:split_index].strip().lstrip("\ufeff")
        return Highlight(title=title, author=author, content=line[2].strip())
