from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if text_type == TextType.TEXT:
            new_nodes.extend(old_node)
        else:
            split_list = old_node.split(delimiter, 2)
            new_nodes.extend(TextNode(split_list[0], text_type=TextType.TEXT))
            new_nodes.extend(TextNode(split_list[1], text_type))
            new_nodes.extend(TextNode(split_list[2], TextType.TEXT))
    return new_nodes

#testing