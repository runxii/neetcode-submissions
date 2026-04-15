# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
''' discussion
- Should the nodes be in the same structure?
- If subroot is an empty tree?
'''


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(n1,n2):
            if not n1 or not n2:
                return n1 is n2
            elif n1.val!=n2.val:
                return False
            return same(n1.left,n2.left) and same(n1.right,n2.right)
        def dfs(r,sr):
            if r is None:
                return r is sr
            if same(r,sr):
                return True
            return dfs(r.left,sr) or dfs(r.right,sr)
        return dfs(root,subRoot)



            