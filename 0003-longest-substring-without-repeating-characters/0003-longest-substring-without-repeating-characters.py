class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se=set()
        m,st=0,0
        for i,c in enumerate(s):
            while c in se:
                se.remove(s[st])
                st+=1
            se.add(c)
            m=max(m,i-st+1)
        return m