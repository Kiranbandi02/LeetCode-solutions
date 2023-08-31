class Solution:
    def sortVowels(self, s: str) -> str:
        d="aeiouAEIOU"
        l=[]
        for i in list(s):
            if(i in d):
                l.append(i)
        l.sort()
        j=0
        k=""
        for i in s:
            if(i in d):
                k+=l[j]
                j+=1
            else:
                k+=i
        return k