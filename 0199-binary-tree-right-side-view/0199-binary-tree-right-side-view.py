# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def h(root,d):
            if root:
                if(d==len(l)):
                    l.append(root.val)
                h(root.right,d+1)
                h(root.left,d+1)
        l=[]
        h(root,0)
        return l
                