# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
''' discussion
- if a right side node has only left child, return the left child or not?
- for an empty tree, return []?
'''
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ''' 
        1. brute force: traverse from root, get root.right if exist, else root.left
        when root.right is None and root.left is None, add root.val to res, stop
        Time complexity: O(h) (height)
        '''
        if root is None:
            return []
        rv=[]
        q=deque()
        q.append(root)
        while q:
            size=len(q)
            level=[]
            for i in range(size):
                p=q.popleft()
                
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
                level.append(p.val)
            rv.append(level[-1])
        return rv