# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' discussion
- is an empty tree legit?
- root is the only node in the tree, return 0 or 1?
- Does root count in the path?
'''

class Solution:
    def __init__(self):
        self.res=0
        # path max
        self.pm=float('-inf')
    def traverse(self, root: TreeNode):
        if root is None:
            return
        lastPm=self.pm
        self.pm=max(root.val,self.pm)
        if root.val>=self.pm:
            self.res+=1
            print(f'parent max: {lastPm}, current max: {self.pm}, root: {root.val}')
        self.traverse(root.left)
        self.traverse(root.right)
        self.pm=lastPm

    def goodNodes(self, root: TreeNode) -> int:
        ''' approach
        1. brute force: record the path for every node while traversing, time would be O(n*h)
        2. if record max value instead of all nodes through the path, it can be improved to O(n)
            - suppose every TreeNode can record max value through the path
            - compute maxV for the subtree of the node: cur.max=(cur.val, parent.max)
            - if cur.val>=cur.max: res+=1
            - if cur.val<cur.max: continue the traversal
        3. if the structure of TreeNode cannot be modified, use a var `pathMax`:
            - set pathMax=root.val (if root is None: return 0)
            - preorder position (entering a node): compute max
            - postorder position (leaving a node): set pathMax to last version
        '''
        self.traverse(root)
        return self.res
        
        
