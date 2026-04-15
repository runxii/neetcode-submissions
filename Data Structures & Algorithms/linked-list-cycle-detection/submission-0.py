# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c=head
        # visited node
        vn=set()
        while c is not None:
            vn.add(c)
            c=c.next
            if c in vn:
                return True
                break 
        return False