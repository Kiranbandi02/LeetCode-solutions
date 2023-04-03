class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        c=0
        i,j=0,len(p)-1
        p.sort()
        while(i<=j):
            c+=1
            if(p[i]+p[j]<=limit):
                i+=1
            j-=1
        return c