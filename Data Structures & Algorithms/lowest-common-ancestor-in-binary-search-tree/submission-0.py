# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
''' discussion
- What to return when p or q not in the tree?
- What if p is the ancestor of q or vice versa?
- Could p be the same with q?
- Do nodes with same values exist in the BST?
'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ''' 
        1. brute force: traverse from root, compare p and q with root:
            - if both < root, move root to left subtree
            - if p<root, q>root, this is the lca
            - if both > root, move root to right subtree
           Boolean diffSide=p<root XOR q<root:
            - diffSide is True, different subtree, stop, return current root
            - diffSide is False, same subtree, keep traversing until diffSide is True
           Time complexity: worst O(log n)
        '''
        
        def dfs(r):
            if r is None:
                return
            # knowing the info of root node, already entered, inorder position
            if r.val==p.val:
                print(f'type of root is {type(r)}, root: {r.val}, p: {p.val}')
                return r
            if r.val==q.val:
                return r
            diff=(p.val<r.val)^(q.val<r.val)
            print(f'root: {r.val}, p: {p.val}, q: {q.val}')
            if diff==True:
                return r
            elif diff==False:
                # both in left subtree
                if p.val<r.val:
                    return dfs(r.left)
                elif p.val>r.val:
                    return dfs(r.right)
        return dfs(root)