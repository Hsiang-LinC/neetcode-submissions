# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
            sum of subtrees and node itself.
            need to consider negative values --> early stop
            keep global max
        '''
        curMax = root.val

        def dfs(root) -> int:
            if not root:
                return 0
            
            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs(root.right))
            
            nonlocal curMax
            curMax = max(curMax, root.val + leftMax + rightMax)
            
            return max(0, leftMax + root.val, rightMax + root.val)
        dfs(root)
        return curMax

