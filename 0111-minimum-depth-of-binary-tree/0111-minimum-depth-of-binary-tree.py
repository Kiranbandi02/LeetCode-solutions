# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        l=[]
        def h(root,d):
            if root.left is None and root.right is None:
                l.append(d)
                return
            if root.left is not None:
                h(root.left,d+1)
            if root.right is not None:
                h(root.right,d+1)
        if root is None:
            return 0
        h(root,1)
        return min(l)