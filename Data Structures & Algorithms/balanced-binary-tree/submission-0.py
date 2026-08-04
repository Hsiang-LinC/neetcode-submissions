'''
    Given a binary tree, return true if it is height-balanced and false otherwise.
    A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        '''
            1. for every nodes, check if left and right subtrees are valid
            2. DP, recursive.
        '''
        def dfs(node: TreeNode | None) -> int:
            # base case
            if not node:
                return 0

            left_height = dfs(node.left)
            if left_height == -1:
                return -1

            right_height = dfs(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        node = root
        return dfs(node) != -1
