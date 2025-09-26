from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
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
        
def text_node_to_html_node(node):
    match node.text_type:
        case TextType.BOLD:
            return LeafNode("b", node.text)
        case TextType.ITALIC:
            return LeafNode("i", node.text)
        case TextType.CODE:
            return LeafNode("code", node.text)
        case TextType.LINK:
            props = "" if node.url is None else node.url
            return LeafNode("a", node.text,{"href": props})
        case TextType.IMAGE:
            url = "" if node.url is None else node.url
            props = "" if node.text is None else node.text
            return LeafNode("img", "", {"src": url, "alt": props})
        case TextType.TEXT:
            return LeafNode(None, node.text)
    raise Exception("Unknown TextType")