# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l=[]
        def h(root):
            if(root is None):
                return
            l.append(root.val)
            h(root.left)
            h(root.right)
        h(root)
        l.sort()
        d=[]
        for i in range(len(l)-1):
            d.append(abs(l[i]-l[i+1]))
        return min(d)