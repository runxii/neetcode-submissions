# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)
        dummy=ListNode(-1)
        d=dummy
        if n==0:
            d.next=None
            return dummy.next
        if n==1:
            d.next=lists[0]
            return dummy.next
        # max num right now
        while True:
            minNode=-1
            for i in range(n):
                cur=lists[i]
                if cur is None:
                    continue
                if minNode==-1 or lists[minNode].val>cur.val:
                    minNode=i
            # All lists is None
            if minNode==-1:
                break
            d.next=ListNode(lists[minNode].val)
            d=d.next
            lists[minNode]=lists[minNode].next


    
        return dummy.next

        
            
