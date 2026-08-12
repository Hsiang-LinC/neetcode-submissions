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
        def dfs(node: TreeNode | None, curMax: int) -> int:
            if node is None:
                return 0

            isGood = node.val >= curMax
            curMax = max(node.val, curMax)

            return isGood + dfs(node.left, curMax) + dfs(node.right, curMax)
        return dfs(root, root.val)
        
            
            