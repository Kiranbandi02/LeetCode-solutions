# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d,d1=head,head
        l=[]
        while d:
            l.append(d.val)
            d=d.next
        for i in range(len(l)):
            j=i
            while j>0 and l[j-1]>l[j]:
                l[j-1],l[j]=l[j],l[j-1]
                j-=1
        i=0
        while d1:
            d1.val=l[i]
            i+=1
            d1=d1.next
        return head