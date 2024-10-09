"""Something to parse"""
from typing import List

from fastapi import UploadFile

from model.models import Highlight


class Parser:
    """Parse me baby one more time"""

    def __init__(self, file: UploadFile):
        self.file = file

    def parse(self) -> List[Highlight]:
        """Something wicked this way comes"""
        res = self.file.file.read().decode().split("==========")
        return [mapper(r) for r in res]


def mapper(chunk: str) -> Highlight:
    line = chunk.split("\n")
    split_index = line[0].rfind("(")
    author = line[split_index:][0].replace(")", "")
    title = line[:split_index]
    return Highlight(title, author, line)
