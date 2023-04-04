class Solution:
    def maxProfit(self, p: List[int]) -> int:
        pr=0
        mi=p[0]
        for i in range(1,len(p)):
            c=p[i]-mi
            pr=max(c,pr)
            mi=min(p[i],mi)
        return pr