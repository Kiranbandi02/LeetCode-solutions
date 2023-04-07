# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        st=ListNode(-1)
        est=ListNode(-1)
        k,k1=st,est
        while head:
            if(head.val>=x):
                est.next=head
                est=est.next
            else:
                st.next=head
                st=st.next
            head=head.next
        est.next=None
        st.next=k1.next
        return k.next
                
        