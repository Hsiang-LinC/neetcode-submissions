# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
            build hashmap to avoid linear time index search
            pass index of left and right instead of slicing (linear op)
        '''
        if not preorder:
            return
        
        pos = {}    # position dict
        for i, val in enumerate(inorder):
            pos[val] = i
        
        def build(start, left, right):
            if left >= right:
                return None
            
            root = TreeNode(preorder[start])
            mid = pos[root.val]
            left_size = mid - left

            root.left = build(start + 1, left, mid)
            root.right = build(start + left_size + 1, mid + 1, right)
            
            return root
        return build(0, 0, len(inorder))






