"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d=head
        e=head
        a=Node(-1)
        k=a
        c=0
        while d:
            a.next=Node(d.val)
            a=a.next
            d=d.next
            c+=1
        l=[]
        while e:
            if(e.random==None):
                l.append(-1)
                e=e.next
                continue
            r=e.random
            i=0
            while r:
                i+=1
                r=r.next
            l.append(c-i)
            e=e.next
        d1=k.next
        for i in l:
            b=k.next
            j=0
            if(i==-1):
                d1.random=None
            else:
                while i!=j:
                    b=b.next
                    j+=1
                d1.random=b
            d1=d1.next
        return k.next
            
        
        
        