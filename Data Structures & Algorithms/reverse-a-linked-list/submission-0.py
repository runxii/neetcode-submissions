# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        current=head
        vals=[head.val]
    
        while current.next!=None:
            current=current.next
            vals.append(current.val)
        
        print(vals)
        current=head
        while len(vals)!=0:
            current.val=vals.pop()
            current=current.next

        return head
            