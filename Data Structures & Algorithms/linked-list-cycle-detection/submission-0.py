# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
            trivial sol: use a hash set to check existance
            constant space complexity: mark on traversed nodes
            e.g., change the value oob, or change the link
        '''

        cur = head
        while cur:
            if cur.next == cur:
                return True
            
            nxt = cur.next
            cur.next = cur
            cur = nxt
        return False