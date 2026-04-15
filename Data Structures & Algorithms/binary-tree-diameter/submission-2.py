# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
''' discussion
- for every node, the diameter is the height(left)+height(right)
- brute force is O(N^2), computing the height for every node
- from the leaf node, compute the height and compare with maxDiameter
'''
class Solution:
    def diameterOfBinaryTree(self, root):
        self.dia = 0

        def dfs(node):
            # 返回：从 node 向下到叶子的高度（边数）
            if not node:
                return 0

            lh = dfs(node.left)
            rh = dfs(node.right)

            # 直径经过当前节点
            self.dia = max(self.dia, lh + rh)

            return 1 + max(lh, rh)

        dfs(root)
        return self.dia
