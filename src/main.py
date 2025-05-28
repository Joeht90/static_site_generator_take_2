
from textnode import TextNode

def main():
    new_node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(new_node.__repr__())


if __name__ == "__main__":
    main()