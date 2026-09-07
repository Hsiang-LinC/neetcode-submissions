# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        '''
            start with n1 -> n2 -> None
            become n2 -> n1 -> None
        '''
        prv = None
        while head:
            nxt = head.next
            head.next = prv
            prv = head
            head = nxt 
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        '''
            start: sp -> n1 -> ... -> nk = fp
            after: sp -> nk -> ... -> n1 -> fp, let sp = n1
        '''
        dummy = sp = fp = ListNode(0, head)
        count = 0
        while fp:
            if count == k:
                n1 = sp.next
                nxt = fp.next
                fp.next = None
                self.reverseList(n1)

                n1.next = nxt
                sp.next = fp
                sp = fp = n1
                count = 0
            fp = fp.next
            count += 1
        
        return dummy.next
                