# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        
        # print(f'The linked list has {n} nodes, slow at {s.val}, fast at {f.val}')
        # half1: [head -> slow], half2: (slow -> fast] 
        prv=None
        h2=s.next
        s.next=None
        while h2!=None:
            nxt=h2.next
            h2.next=prv
            prv=h2
            h2=nxt
        h2=prv
        
        # print(f'Reversed half2 head at {h2.val}')
        h1=head
        while h2 is not None:
            nxt1=h1.next
            nxt2=h2.next
            h2.next=nxt1
            h1.next=h2
            h1=nxt1
            h2=nxt2