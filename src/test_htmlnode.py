import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(value="This is a text node", props={"href": "https://www.google.com",
                                                               "target": "_blank"})


if __name__ == "__main__":
    unittest.main()
