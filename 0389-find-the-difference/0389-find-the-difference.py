from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res=""
        d_s=Counter(s)
        d_t=Counter(t)
        for i in d_t:
            if d_s[i]!=d_t[i]:
                res+=i
        return res