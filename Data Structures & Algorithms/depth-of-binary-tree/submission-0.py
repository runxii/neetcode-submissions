# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def __init__(self):
        # max depth
        self.md=0
        # depth
        self.dp=0
    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.dp+=1
        if root.left is None and root.right is None:
            self.md=max(self.md, self.dp)
        self.traverse(root.left)
        self.traverse(root.right)
        self.dp-=1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.md