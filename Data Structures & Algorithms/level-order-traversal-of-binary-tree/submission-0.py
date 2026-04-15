# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
''' discussion
- If a node has only one child node, should we include the nn-exist child node as Null in
the list, or leave it out of the list?
- Empty tree as edge case
'''

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=deque()
        q.append(root)
        levels=[]
        while q:
            level=[]
            length=len(q)
            i=0
            while i<length:
                if q[i].left is not None:
                    q.append(q[i].left)
                if q[i].right is not None:
                    q.append(q[i].right)
                level.append(q.popleft().val)
                length-=1
            levels.append(level)
        return levels
