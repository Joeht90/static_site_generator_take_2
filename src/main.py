"""
Main file for my static site generator.
So far we only need to import TextNode from textnode.py
"""
from textnode import TextNode

def main():
    """This is just a test to verify the main function is working correctly"""
    new_node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(new_node)


if __name__ == "__main__":
    main()
