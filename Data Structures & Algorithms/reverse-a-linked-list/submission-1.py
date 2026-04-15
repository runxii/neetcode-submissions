# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cr=head
        prv=None
        while cr is not None:
            nxt=cr.next
            cr.next=prv
            prv=cr
            cr=nxt
        return prv
            