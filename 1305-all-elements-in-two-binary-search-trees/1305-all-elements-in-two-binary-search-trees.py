# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l=[]
        def he(root):
            if root is None:
                return
            he(root.left)
            l.append(root.val)
            he(root.right)
        he(root1)
        he(root2)
        return sorted(l)
        