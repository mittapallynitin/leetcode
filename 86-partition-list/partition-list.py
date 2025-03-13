# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = l =  ListNode(None)
        second = r =  ListNode(None)

        current = head
        while current:
            node = current 
            current = current.next
            if node.val < x:
                l.next = node
                l = node 
                l.next = None
            else: 
                r.next = node
                r = node
                r.next = None 
        
        l.next = second.next 
        return first.next
