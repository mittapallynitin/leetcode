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
        dummy = Node(-1)
        curr = head
        curr2 = dummy
        mapper = dict()
        while curr:
            new = Node(curr.val)
            mapper[curr] = new
            curr2.next = new
            curr = curr.next
            curr2 = curr2.next
        curr = head
        curr2 = dummy.next
        while curr:
            if curr.random:
                curr2.random = mapper[curr.random]
            curr = curr.next
            curr2 = curr2.next
        return dummy.next
        
       
        