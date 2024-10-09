class Highlight:
    """Highlights"""

    def __init__(self, title, author, content):
        self.__title = title
        self.__author = author
        self.__content = content

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Content: {self.__content}"

    def __repr__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Content: {self.__content}"

    def __eq__(self, other):
        return self.__title == other.__title
