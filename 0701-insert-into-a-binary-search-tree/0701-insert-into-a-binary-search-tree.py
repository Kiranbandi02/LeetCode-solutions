# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def inc(root,val):
            if(root is None):
                root=TreeNode(val)
                return root
            if(val>root.val):
                if(root.right is None):
                    root.right=inc(root.right,val)
                else:
                    inc(root.right,val)
            if(val<root.val):
                if(root.left is None):
                    root.left=inc(root.left,val)
                else:
                    inc(root.left,val)
        if root is None:
            return TreeNode(val)
        inc(root,val)
        return root
            