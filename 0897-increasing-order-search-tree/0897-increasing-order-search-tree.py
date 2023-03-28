# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l=[]
        def h(root):
            if root  is None:
                return
            l.append(root)
            h(root.left)
            h(root.right)
        h(root)
        l=sorted(l,key= lambda x:x.val)
        k=TreeNode(-1)
        a=k
        for i in l:
            k.right=TreeNode(i.val)
            k=k.right
        return a.right