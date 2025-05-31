from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            split_list = old_node.text.split(delimiter, 2)
            # I dont have time to finish this before lunch is over but
            # you can use the index() method to return the index of the list
            # anything between the delimiter will be within an odd number index
            # and anything even will be of TextType.TEXT
            new_nodes.append(TextNode(split_list[1], text_type))
            new_nodes.append(TextNode(split_list[2], TextType.TEXT))
    return new_nodes


