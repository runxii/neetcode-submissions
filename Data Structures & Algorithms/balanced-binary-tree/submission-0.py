# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
''' discussion
- What to return for an empty tree?
'''
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced=True
        def height(node):
            if node is None:
                return 0
            lh=height(node.left)
            rh=height(node.right)
            if abs(lh-rh)>1:
                self.balanced=False
            return 1+max(lh,rh)
        height(root)
        return self.balanced