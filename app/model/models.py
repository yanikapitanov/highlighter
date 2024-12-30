from pydantic import BaseModel


class Highlight(BaseModel):
    """Highlights"""
    title: str | None
    author: str | None
    content: str | None

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Content: {self.content}"

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Content: {self.content}"

    def __eq__(self, other):
        return self.title == other.__title

    def __hash__(self):
        return hash(self.content)
