# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bal(root):
            if root is None:
                return 0
            return max(bal(root.left),bal(root.right))+1
        if root is None:
            return 1
        if root.left is None and root.right is None:
            return 1
        l=bal(root.left)
        h=bal(root.right)
        return abs(l-h)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        