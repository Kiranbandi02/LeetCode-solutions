# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        k=head
        l=[]
        while k:
            l.append(k.val)
            k=k.next
        i=0
        j=head
        while j:
            j.val=l.pop(i)
            if(i==0):
                i=-1
            else:
                i=0
            j=j.next
        
        