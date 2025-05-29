"""
These are unittests for the htmlnode.py
"""
import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    """Do I really have to put things here for the problems to go away?"""
    def test_to_html_props(self):
        """Jesus it's going to make me do this for every method."""
        node = HTMLNode(
            "div",
            "hello",
            None,
            {"class": "greeting", "href": "https//boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https//boot.dev"'
        )

    def test_props_to_html_single_attribute(self):
        """
        Well I guess I will have to start making this a habit or else 
        I am going to lose my shit
        """
        node = HTMLNode(
            "span",
            "world",
            None,
            {"id": "intro"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' id="intro"'
        )

    def test_props_to_html_multiple_attributes(self):
        node = HTMLNode(
            "a",
            "click here",
            None,
            {"class": "link", "target": "_blank", "rel": "noopener"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="link" target="_blank" rel="noopener"'
        )

    def test_props_to_html_no_attributes(self):
        node = HTMLNode(
            "p",
            "This is a paragraph.",
            None,
            {}
        )
        self.assertEqual(
            node.props_to_html(),
            ''
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_all_values(self):
        node = HTMLNode(
            "a",
            "Click me",
            children=[],
            props={"href": "https://example.com"}
        )
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click me")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"href": "https://example.com"})

    def test_tag_only(self):
        node = HTMLNode("section")
        self.assertEqual(node.tag, "section")
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_children_only(self):
        child = HTMLNode("p", "Paragraph")
        node = HTMLNode(
            "div",
            children=[child]
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, [child])
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_repr_all_fields(self):
        child = HTMLNode("span", "Nested")
        node = HTMLNode(
            "div",
            "Container",
            children=[child],
            props={"id": "container"}
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(div, Container, children: [HTMLNode(span, Nested, children: None, None)]" \
            ", {'id': 'container'})"
        )

    def test_repr_minimal(self):
        node = HTMLNode(
            "h1",
            "Title"
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(h1, Title, children: None, None)"
        )

    def test_repr_empty_children_and_props(self):
        node = HTMLNode(
            "ul",
            None,
            children=[],
            props={}
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(ul, None, children: [], {})"
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()
