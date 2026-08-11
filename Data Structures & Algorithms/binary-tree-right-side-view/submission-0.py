# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
            BFS, append only the last node of each level
        '''
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            added = False
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    if added:
                        res.pop()
                    res.append(node.val)
                    added = True
        return res
        
            