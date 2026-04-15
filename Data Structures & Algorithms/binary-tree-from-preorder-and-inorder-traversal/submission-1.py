# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # number of nodes
        n=len(preorder)
        rootVal=preorder[0]
        root=TreeNode(rootVal)
        # every node in inorder before root is in left subtree, and after in right subtree
        ri=0
        while ri<n:
            if inorder[ri]==rootVal:
                break
            else:
                ri+=1
        # left subtree
        lst=inorder[0:ri]
        # right subtree
        rst=inorder[ri+1:n]
        # no left subtree nor right subtree
        if len(lst)==0 and len(rst)==0:
            return root
        elif len(lst)==0:
            root.right=self.buildTree(preorder[1:n],rst)
            return root
        elif len(rst)==0:
            # left root value
            lrv=preorder[1]
            root.left=self.buildTree(preorder[1:n],lst)
            return root
        else:
            root.left=self.buildTree(preorder[1:ri+1],lst)
            root.right=self.buildTree(preorder[ri+1:n],rst)
            return root
            