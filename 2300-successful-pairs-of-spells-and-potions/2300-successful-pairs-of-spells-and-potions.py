class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        from math import ceil
        def b(l,h,t):
            if l<=h:
                m=(l+h)//2
                if(potions[m]==t):
                    return m
                if(potions[m]>t):
                    return b(l,m-1,t)
                if(potions[m]<t):
                    return b(m+1,h,t)
            else:
                return -1
        a=[]
        potions.sort()
        l=len(potions)-1
        for i in spells:
            c=0
            d=ceil(success/i)
            if(d>potions[-1]):
                a.append(0)
            else:
                a.append(l-bisect.bisect_left(potions,d)+1)
        return a
