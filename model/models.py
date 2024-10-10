class Highlight:
    """Highlights"""

    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Content: {self.content}"

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Content: {self.content}"

    def __eq__(self, other):
        return self.title == other.__title
