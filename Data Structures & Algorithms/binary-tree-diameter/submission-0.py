# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
            observation:
            1. it must be leaf to leaf, otherwise can be lengthen
            2. must share a common root node in a subtree
            3. must on different side of the root

            key:
            find max right height + left height
            height = max(right, left) + 1
            one var for left + right
        '''
        max_diam = 0
        def dfs(node: TreeNode | None) -> int:
            nonlocal max_diam
            right_height = dfs(node.right) + 1 if node.right else 0
            left_height = dfs(node.left) + 1 if node.left else 0

            max_diam = max(max_diam, right_height + left_height)
            return max(right_height, left_height)
        dfs(root)

        return max_diam