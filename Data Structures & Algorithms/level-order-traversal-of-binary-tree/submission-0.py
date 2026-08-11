# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
            BFS --> FIFO
            Python: collections.deque()
            deque.append, deque.popleft
        '''
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            nodeList = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    nodeList.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if nodeList:
                res.append(nodeList)
        return res