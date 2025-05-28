class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError ("Child classes will override")

    def props_to_html(self):
        return f" {self.tag} {self.value} {self.children} {self.props}"
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, childre={self.children}, props={self.props})"
