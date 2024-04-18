class Node:
    """
    A linked list is a collection of nodes
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)


