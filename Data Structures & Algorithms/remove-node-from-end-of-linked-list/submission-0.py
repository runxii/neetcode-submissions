# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r=head
        i=1
        while i<n:
            r=r.next
            i+=1
        l=ListNode()
        l.next=head
        while r and r.next:
            r=r.next
            l=l.next
        nxt=l.next
        l.next=nxt.next
        if nxt==head:
            return l.next
        return head
            