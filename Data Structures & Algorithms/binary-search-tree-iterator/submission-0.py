# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # when initialized, the pointer automatically goes to a dummy head, and next is the smallest node in BST
        self.st=[]
        self.cur=root

        while self.cur:
            self.st.append(self.cur)
            self.cur=self.cur.left
        # now cur is null, and pointer is at a dummy smallest number
        # print(f'initialized, call stack: {self.st}, current at {self.cur}')

    def next(self) -> int:
        # when cur is none, go back and pop the call stack
        if self.cur is None:
            self.cur=self.st.pop()
            return self.cur.val
        # if cur is not null, go to the right subtree
        self.cur=self.cur.right
        while self.cur:
            self.st.append(self.cur)
            self.cur=self.cur.left
        # current cur is null, should pop one from call stack
        self.cur=self.st.pop()
        return self.cur.val
    def hasNext(self) -> bool:
        print(f'current stack: {self.st}, current at {self.cur}')
        if len(self.st)==0 and self.cur.right is None:
            return False
        return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()