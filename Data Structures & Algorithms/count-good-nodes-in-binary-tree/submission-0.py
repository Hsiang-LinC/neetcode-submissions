# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
            DFS traverse
            Keep track of current max
        '''
        res = []
        
        def dfs(node: TreeNode | None, curMax: int):
            if node is None:
                return
            if node.val >= curMax:
                res.append(node.val)
                curMax = node.val
            return dfs(node.left, curMax), dfs(node.right, curMax)
        dfs(root, root.val)
        return len(res)
            
            