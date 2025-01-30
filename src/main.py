from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():

    test_textnode = TextNode("Boop the Snoot", TextType.ITALICS, "https://youtu.be/obU8sw2A0MA")

    test_htmlnode = HTMLNode(tag="a", value="text", props={
        "href": "https://www.google.com",
        "target": "_blank"})

    test_leafnode = LeafNode(tag="a", value="text", props={
        "href": "https://www.google.com",
        "target": "_blank"})

    print(test_textnode)

    print(test_htmlnode)

    print(test_leafnode)

    print(test_leafnode.to_html())

if __name__ == "__main__":
    main()
