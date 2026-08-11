# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p: TreeNode | None, q: TreeNode | None) -> bool:
            if not p or not q:
                return p is q
            return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)
        
        def isMatch(p: TreeNode | None, q: TreeNode | None) -> bool:
            if not p or not q:
                return p is q
            if p.val == q.val:
                return isSame(p, q) or isMatch(p.right, q) or isMatch(p.left, q)
            else:
                return isMatch(p.right, q) or isMatch(p.left, q)
        
        return isMatch(root, subRoot)