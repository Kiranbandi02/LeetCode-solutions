# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        l=[]
        if(head is None):
            return None
        while head:
            l.append(head.val)
            head=head.next
        l1,f=0,len(l)-1
        def build(a,b):
            if a>b:
                return None
            mid=(a+b)//2
            node=TreeNode(l[mid])
            node.left=build(a,mid-1)
            node.right=build(mid+1,b)
            return node
        return build(l1,f)