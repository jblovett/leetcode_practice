# Definition for a binary tree node.
"""Problem 104: https://leetcode.com/problems/maximum-depth-of-binary-tree/.
Binary search trees, heaps, and depth first search perhaps?"""

class TreeNode:
     val: int
     left: TreeNode
     right: TreeNode
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    iterations: int = 0
    
    def maxDepth(self, root: TreeNode) -> int:
        # base case: found the deepest leaf
        # self.left = null
        depth: int
        if root.left == None and root.right == None:
            depth += 1
            return depth
        elif root.left == None:
            