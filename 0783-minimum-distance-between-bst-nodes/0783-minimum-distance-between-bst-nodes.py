# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        l=[]
        def ino(root):
            if root :
                ino(root.left)
                l.append(root.val)
                ino(root.right)
            return 
        ino(root)
        m=[float('inf')]
        for i in range(1,len(l)):
            m.append(l[i]-l[i-1])
        return min(m)