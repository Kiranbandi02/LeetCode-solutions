# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        l=[]
        while(cur):
            l.append(cur.val)
            cur=cur.next
        l.sort()
        a=head
        i=0
        while(a):
            a.val=l[i]
            a=a.next
            i=i+1
        return head