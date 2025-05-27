# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        carry = 0

        while l1 and l2:
            s = l1.val + l2.val + carry 
            node =  ListNode(s % 10)
            carry = s // 10
            curr.next = node
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        rem = l1 or l2

        while rem:
            s = rem.val + carry
            node = ListNode(s % 10)
            carry = s // 10 
            curr.next = node
            curr = curr.next
            rem = rem.next 
        
        if carry:
            curr.next = ListNode(carry)

        return dummy.next
        