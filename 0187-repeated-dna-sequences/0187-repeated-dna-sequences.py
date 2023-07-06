class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i=0
        n=len(s)
        d={}
        while(i+10<=n):
            k=s[i:i+10]
            if(k in d):
                d[k]+=1
            else:
                d[k]=1
            """for j in range(i+1,n):
                if(j+10>n):
                    break
                if(s[j:j+10]==s[i:i+10] and s[i:i+10] not in l):
                    l.append(s[i:i+10])
                    break"""
            i+=1
        l=[]
        for i in d:
            if(d[i]>1):
                l.append(i)
        return l