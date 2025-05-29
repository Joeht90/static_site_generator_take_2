import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("Another test but not equal", TextType.ITALIC)
        node4 = TextNode("This will not equal the previous", TextType.ITALIC)
        self.assertNotEqual(node3, node4)

        node5 = TextNode("Another equal test", TextType.CODE)       
        node6 = TextNode("Another equal test", TextType.CODE)
        self.assertEqual(node5, node6)

        node7 = TextNode("This one will have a different texttype", TextType.BOLD)
        node8 = TextNode("This one will have a different texttype", TextType.CODE)
        self.assertNotEqual(node7, node8)
    

class TestTextNodeToHTMLNode(unittest.TestCase):    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, None)

    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertEqual(html_node.props, None)

    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertEqual(html_node.props, None)

    def test_code(self):
        node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")
        self.assertEqual(html_node.props, None)

    def test_link(self):
        node = TextNode("Click here", TextType.LINK, url="https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, None)

    def test_image(self):
        node = TextNode("An image", TextType.IMAGE, url="https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {
            "src": "https://example.com/image.png",
            "alt": "An image"
        })

    def test_invalid_type_raises_value_error(self):
        class FakeType:
            pass
        node = TextNode("Oops", FakeType())
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()