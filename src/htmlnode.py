from typing import Optional

class HTMLNode:
    def __init__(self,
                 tag: Optional[str] = None,
                 value: Optional[str] = None,
                 children: Optional[list] = None,
                 props: Optional[dict] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented")

    def props_to_html(self):
        props_str = ""
        if self.props == None:
             return ""
        for k, v in self.props.value():
            props_str += f" {k}=\"{v}\""
        return props_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
