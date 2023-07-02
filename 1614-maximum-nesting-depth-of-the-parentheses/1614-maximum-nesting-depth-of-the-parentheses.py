class Solution:
    def maxDepth(self, s: str) -> int:
        le,r=0,0
        for i in s:
            if(i=="("):
                le+=1
            elif(i==")"):
                le-=1
            r=max(r,le)
        return r