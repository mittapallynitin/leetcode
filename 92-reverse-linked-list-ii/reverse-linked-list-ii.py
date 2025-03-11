# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, curr = dummy, head

        for _ in range(l - 1):
            left, curr = left.next, curr.next
        
        begin = curr
        prev = None
        for _ in range(r-l+1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        left.next = prev
        begin.next = curr
        return dummy.next




        