"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given a root, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.
"""

"""Definition for a binary tree node."""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    global counter: int = 0

    def maxDepth(self, root: TreeNode) -> int:
        counter += 1
        left: TreeNode = root.left
        right: TreeNode = root.right

        if left == None & right == None:
            return self
        elif (left == None):
            maxDepth(right)
        elif (right == None):
            maxDepth(left)
        else:
            if (maxDepth(left) > maxDepth(right)):
                return left
            else:
                return right