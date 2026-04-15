"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # new head
        nh=Node(0)
        # current
        cr=head
        # new current
        ncr=nh
        # mapping address
        hm={None:None}
        while cr:
            # new node
            ncr.next=Node(cr.val)
            ncr=ncr.next
            hm[cr]=ncr
            cr=cr.next
            
            
        # print(hm)
        ncr=nh.next
        cr=head
        while ncr:
            #print(f'old list current: {cr}, random: {cr.random};\n new list current: {ncr}, random: {ncr.random}')
            ncr.random=hm[cr.random]
            cr=cr.next
            ncr=ncr.next
        return nh.next