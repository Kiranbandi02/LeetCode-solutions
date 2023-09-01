class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[0]*(n+1)
        for i in range(n+1):
            a[i]=bin(i)[2:].count("1")
        return a