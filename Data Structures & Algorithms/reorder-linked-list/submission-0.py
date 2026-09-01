'''
You are given the head of a singly linked-list.
The positions of a linked list of length = 7 for example, can intially be represented as:
[0, 1, 2, 3, 4, 5, 6]
Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]
Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
[0, n-1, 1, n-2, 2, n-3, ...]
You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
            Need to reverse the second half of the linked list
            Can be done with Fast and Slow pointer
            Then merge the 2 linked lists
            Note: verify the odd and even cases, which determine what define second half
        '''
        # edge case:
        if not head or not head.next:
            return

        fp, sp = head.next, head
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
            
        # close the left part
        tmp = sp.next
        sp.next = None

        # reverse right part
        sp = tmp # size(left) = size(right) or size(right)+1
        prev = None
        while sp:
            nxt = sp.next
            sp.next = prev
            prev = sp
            sp = nxt

        # reordered merge
        first, second = head, prev
        while second:
            nxt = first.next
            first.next = second
            second = nxt
            first = first.next
