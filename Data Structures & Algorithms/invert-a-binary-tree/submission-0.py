# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
            invert right and left child nodes of any nodes
            BFS?
        '''
        def dfs(node):
            if not node:
                return
            tmp = node.left
            node.left = node.right
            node.right = tmp

            dfs(node.right)
            dfs(node.left)
        
        dfs(root)
        return root
