from enum import Enum

class TextType(Enum):
    TEXT = "Plain text"
    BOLD = "**text**"
    ITALIC = "_text_"
    CODE = "`code`"
    LINK = "[anchor text](url)"
    IMAGE = "[alt text](url)"
    
class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL = None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL

    def __repr__(self):
        return f"TextNode(text='{self.text}', type={self.text_type.name}, url={self.url})"

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
