import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()