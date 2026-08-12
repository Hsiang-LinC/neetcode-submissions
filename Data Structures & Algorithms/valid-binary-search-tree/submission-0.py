# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
            For every node we traverse in DFS, 2 contraints for both right and left subtree.
            1. rightMax > right > node
            2. leftMin < left < node
        '''
        
        def dfs(node: TreeNode | None, leftMin: int, rightMax: int) -> bool:
            if node is None:
                return True
            if not rightMax > node.val > leftMin:
                return False
            
            leftMin = min(leftMin, node.val)
            rightMax = max(rightMax, node.val)
            
            return dfs(node.left, leftMin, node.val) and dfs(node.right, node.val, rightMax)
        
        return dfs(root, -10000000000, 1000000000)