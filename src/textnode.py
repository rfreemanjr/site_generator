class TextNode():
    #constructor for the TextNode
    # The url will default to None is nothing is provided
    def __init__(self, text, t_type, url=None):
        self.text = text
        self.t_type = t_type
        self.url = url
    #This method tests if this node is equal to another node
    def __eq__(self,t_node):
        return (
            self.text == t_node.text and 
            self.url == t_node.url and
            self.t_type == t_node.t_type)
    #This method prints out the data of the particular node.
    def __repr__(self):
        return f"TextNode({self.text}, {self.t_type}, {self.url})"