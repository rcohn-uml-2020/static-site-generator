from enum import Enum
from typing import Optional

class TextType(Enum):
    NORMAL = "Normal"
    BOLD = "Bold"
    ITALICS = "Italics"
    CODE = "Code"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: Optional[str] = None):
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        if not isinstance(text_type, TextType):
            raise TypeError("text_type must be a TextType")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(node1, node2):
        return (node1.text == node2.text) & (node1.text_type == node2.text_type) & (node1.url == node2.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
