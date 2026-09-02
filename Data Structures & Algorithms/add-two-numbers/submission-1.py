# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        carry = 0
        while True:
            sum = cur1.val + cur2.val + carry
            carry = sum // 10
            sum = sum % 10
            cur1.val = sum
            
            if cur1.next and cur2.next:
                cur1, cur2 = cur1.next, cur2.next
            else:
                break
        
        if cur2.next:
            cur1.next = cur2.next
        
        # remaining carry
        while carry:
            if not cur1.next:
                node = ListNode(1)
                cur1.next = node
                return l1
            else:
                cur1 = cur1.next
                sum = cur1.val + carry
                carry = sum // 10
                cur1.val = sum % 10
        return l1


            