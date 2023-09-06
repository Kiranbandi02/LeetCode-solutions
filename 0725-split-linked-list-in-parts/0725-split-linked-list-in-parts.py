# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur=root
        c=0
        while cur:
            c+=1
            cur=cur.next
        w,r=divmod(c,k)
        cur=root
        l=[]
        for i in range(k):
            ne=ListNode(-1)
            a=ne
            for j in range(w+(i<r)):
                ne.next=ListNode(cur.val)
                ne=ne.next
                if(cur):
                    cur=cur.next
            l.append(a.next)
        return l