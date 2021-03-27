"""Finding the maximum depth of a binary tree.

For this question, depth is based on the maximum number of nodes one can reach
until one hits a leaf.
"""


from __future__ import annotations

__author__: str = "christineiym"


class TreeNode:
    val: int
    left: TreeNode
    right: TreeNode

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    #TODO: Define setLeft, setRight
    #TODO: Implement BST
    

class Solution:
    root: TreeNode

    def __init__(self, root=None):
        root = root
        # TODO: complete

    def maxDepth(self, root: TreeNode) -> int:
        left: TreeNode = root.left
        right: TreeNode = root.right

        if self == None:
            return 0
        
        else:
            return (1 + max(maxDepth(self, root.left), maxDepth(self, root.right)))