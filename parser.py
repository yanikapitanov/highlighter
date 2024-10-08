from typing import List

from fastapi import UploadFile

from model.highlight import Highlight


class Parser:
    def __init__(self, file: UploadFile):
        self.file = file


    def parse(self) -> List[Highlight]:
        res = self.file.file.read().decode().split("==========")
        [print(h) for h in res]
        return []
