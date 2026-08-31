# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        # start with smallest init for cur1
        if list1.val <= list2.val:
            cur1, cur2 = list1, list2
        else:
            cur1, cur2 = list2, list1
        
        while cur1.next:
            if cur1.next.val <= cur2.val:
                cur1 = cur1.next
            else:
                tmp = cur1.next
                cur1.next = cur2
                cur2 = tmp
                cur1 = cur1.next
        cur1.next = cur2
        
        if list1.val <= list2.val:
            return list1
        else:
            return list2
        