class Solution:
    def beautySum(self, s: str) -> int:
        from collections import Counter
        l=[]
        sum=0
        n=len(s)
        for i in range(len(s)):
            for j in range(i+1,n+1):
                c=Counter(s[i:j])
                sum+=(max(c.values())-min(c.values()))
        return sum
                