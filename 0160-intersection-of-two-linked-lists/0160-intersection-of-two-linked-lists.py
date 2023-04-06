# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d1=headA
        d2=headB
        l1,l2=0,0
        while d1:
            l1+=1
            d1=d1.next
        while d2:
            l2+=1
            d2=d2.next
        d1=headA
        d2=headB
        if(l1>l2):
            i=0
            while(i!=l1-l2):
                d1=d1.next
                i+=1
        elif(l2>l1):
            i=0
            while(i!=l2-l1):
                d2=d2.next
                i+=1
        while(d1 and d2):
            if(d1==d2):
                return d1
            d1=d1.next
            d2=d2.next
        return d1