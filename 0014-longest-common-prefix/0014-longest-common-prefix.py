class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        strs=sorted(strs)
        for i,j in zip(strs[0],strs[-1]):
            if(i!=j):
                break
            s+=i
        return s