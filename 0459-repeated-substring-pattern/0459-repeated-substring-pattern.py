class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        c=""
        i=0
        while i<len(s):
            c=c+s[i]
            if(c==s[i+1:i+len(c)+1]):
                k=s.count(c)
                if(k*len(c)==len(s)):
                    return 1
            i+=1
        return 0