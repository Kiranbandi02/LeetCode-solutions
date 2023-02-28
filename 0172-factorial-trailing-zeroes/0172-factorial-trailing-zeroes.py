class Solution:
    def trailingZeroes(self, n: int) -> int:
        c=0
        while(n>=5):
            q=n//5
            n=q
            c=c+q
        return c