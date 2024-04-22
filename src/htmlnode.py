class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        #String representing HTML tag name
        self.tag = tag
        #String representing value of HTML tag
        self.value = value
        #List of HTMLNode objects representing children of this node
        self.children = children
        #Dictionary of key-value pairs representing attributes of the HTML tag
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        s = ""
        for key,value in self.props.items:
            s += f" {key}={value}"
        return s
    