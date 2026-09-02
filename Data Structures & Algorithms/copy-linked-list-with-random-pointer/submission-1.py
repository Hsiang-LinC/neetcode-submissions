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
            return
        # hash map to jump directly to the nodes
        nodeDict = {}
        node = Node(head.val)
        nodeDict[head] = node
        cur = head.next
        while cur:
            nextNode = Node(cur.val)
            node.next = nextNode
            node = nextNode
            nodeDict[cur] = node
            cur = cur.next
        
        # create random pointer
        cur = head
        while cur:
            node = nodeDict[cur]
            if cur.random:
                node.random = nodeDict[cur.random]
            else:
                node.random = None
            cur = cur.next
        
        return nodeDict[head]




            