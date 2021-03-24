class BST:
    value: int
    left: BST(None)
    right: BST(None)

    def __init__(self, value: int) -> None:
        """creates an empty BST"""
        self.value = value
        self.left = None
        self.right = None

    def get_left(self) -> BST:
        return self.left

    def get_right(self) -> BST:
        return self.right

    def get_value(self) -> int:
        return self.value

    def insertBST(self, insertion: int) -> BST:
        if insertion < self.get_value():
            if self.get_left == None:
                self.left = BST(insertion)
                return self
            else:
                return self.get_left().insertBST(insertion)
        elif insertion >= self.get_value():
            if self.get_right == None:
                self.right = BST(insertion)
                return self
            else:
                return self.get_right().insertBST(insertion)

        
            
        