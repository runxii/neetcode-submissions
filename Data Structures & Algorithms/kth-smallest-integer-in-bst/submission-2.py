# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st=[]
        cur=root
        while cur or st:
            # push the left spine until null
            while cur:
                st.append(cur)
                cur=cur.left
            # cur is None, pop one and visit right
            cur=st.pop()
            k-=1
            res=cur.val
            if k==0:
                return res
            cur=cur.right
        # return -1 if k is invalid
        return -1