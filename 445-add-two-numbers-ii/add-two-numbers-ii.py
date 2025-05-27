# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr: ListNode):
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp 
            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)

        root = curr = ListNode()
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            curr.next = ListNode(s % 10)
            curr = curr.next
            carry = s // 10
            l1 = l1.next
            l2 = l2.next
        
        rem = l1 or l2 
        while rem:
            s = rem.val + carry
            curr.next = ListNode(s % 10)
            curr = curr.next
            carry = s // 10 
            rem = rem.next 
        
        if carry:
            curr.next = ListNode(carry)
        
        print(root.next)
        
        return reverse(root.next)

        

            
        