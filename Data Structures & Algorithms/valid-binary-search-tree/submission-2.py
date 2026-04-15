# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
''' discussion
- If the key is duplicated, should return false?
- For any tree with only 1 node, it is true
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ''' approach
        1. For each node:
            - all nodes in right subtree>node
            - all nodes in left subtree<node
            - minimal case: the subtree contains only two child nodes: compare vals
        2. Brute force: for each node, traverse through left sub and right sub;
           This cost time O(n^2)
        3. 
        '''
        def less(r,l):
            if l is None:
                return True
            if r.val<=l.val:
                return False
            return less(r,l.left) and less(r,l.right)
        def more(r,rt):
            if rt is None:
                return True
            if r.val>=rt.val:
                return False
            return more(r,rt.left) and more(r,rt.right)
        def dfs(r):
            if r is None:
                return True
            if less(r,r.left)==False or more(r,r.right)==False:
                return False
            return dfs(r.left) and dfs(r.right)

        return dfs(root)
