# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' discussion
- For empty trees, is it same or not?

For every node, if the left&right subtrees are the same, and the val of the node is same
with another node, it is `True`.
To get the full info of left&right subtrees, process at postorder position.
'''

class Solution:
    def isSameNode(self, n1: Optional[TreeNode], n2: Optional[TreeNode])-> bool:
        
        return False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same=True
        def dfs(n1,n2):
            if n1 is None and n2 is None:
                return True
            elif n1 is None and n2 is not None:
                return False
            elif n2 is None and n1 is not None:
                return False
            elif n1.val==n2.val:
                l=dfs(n1.left, n2.left)
                r=dfs(n1.right, n2.right)
                return l and r
            elif n1.val!=n2.val:
                return False
        return dfs(p,q)
            