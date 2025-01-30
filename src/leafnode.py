from typing import Optional
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,
                 tag: Optional[str] = None,
                 value: Optional[str] = None,
                 props: Optional[dict] = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("no value")
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def props_to_html(self):
        props_str = ""
        if self.props == None:
             return ""
        for k, v in self.props.items():
            props_str += f" {k}=\"{v}\""
        return props_str

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
