class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        from math import ceil
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
