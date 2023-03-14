# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        l=[]
        def he(root,s):
            if root is None:
                l.append(s)
                return
            s+=str(root.val)
            if(root.left is None and root.right is None):
                l.append(s)
                return
            if(root.left):
                he(root.left,s)
            if(root.right):
                he(root.right,s)
        he(root,"")
        s=0
        for i in l:
            s+=int(i)
        return s
                        
            
        