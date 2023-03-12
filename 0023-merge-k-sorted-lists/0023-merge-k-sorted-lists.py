# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(lists==[]):
            return None
        k=ListNode(-1)
        d=k
        a=lists.pop(0)
        while lists!=[]:
            b=lists.pop(0)
            while a!=None and b!=None:
                if(a.val<=b.val):
                    k.next=a
                    a=a.next
                elif(b.val<a.val):
                    k.next=b
                    b=b.next
                k=k.next
            while a!=None:
                k.next=a
                a=a.next
                k=k.next
            while b!=None:
                k.next=b
                b=b.next
                k=k.next
            a=d.next
            k=ListNode(-1)
            d=k
        return a
                
                    