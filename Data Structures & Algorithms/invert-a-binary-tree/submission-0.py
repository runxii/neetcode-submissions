# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' discussion
- What if the tree is not balanced?
- complexity constraints?
'''

class Solution:
    def traverse(self, root:Optional[TreeNode]):
        if root is None:
            return
        root.left,root.right=root.right,root.left
        self.traverse(root.left)
        self.traverse(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root