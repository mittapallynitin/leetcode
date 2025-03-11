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
        if not head:
            return None
        
        mapper = {None: None}
        curr = head
        while curr:
            mapper[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            node = mapper[curr]
            node.next = mapper[curr.next]
            node.random = mapper[curr.random]
            curr = curr.next
        return mapper[head]
       
        