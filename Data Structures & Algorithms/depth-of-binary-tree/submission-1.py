# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
            need to explore all nodes, since binary tree might not be balacned.
            dfs exploration, return height.
        '''
        def dfs(node: TreeNode | None) -> int:
            if not node:
                return 0
            
            return max(dfs(node.left), dfs(node.right)) + 1
        
        return dfs(root)