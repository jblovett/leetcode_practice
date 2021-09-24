class Node:
    def __init__(self,value=None):
        self.left_child = None
        self.right_child = None
        self.value = value


class BST:
    def __init__(self,value):
        self.root = None

    def insert_when_empty(self, value):
        if (self.root == None):
            insertion = Node(value)
            self.root = insertion
        else:
            self._insert(value, self.root)


    def _insert(self,value,current_node):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child == Node(value)
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child == Node(value)
            else:
                self._insert(value, current_node.right_child)
