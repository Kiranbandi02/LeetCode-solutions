class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for i in ops:
            if(i[0]<m):
                m=i[0]
            if(i[1]<n):
                n=i[1]
        return m*n