class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        c=0
        d={}
        for i in words:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if(d[i]!=0):
                n,m=len(i),len(s)
                i1,j=0,0
                while(i1<n and j<m):
                    if(i[i1]==s[j]):
                        i1+=1
                    j+=1
                if(i1==n):
                    c+=d[i]
                    d[i]=0
                    
            else:
                c+=1
        return(c)
        
        
        
        
        
        
        """
        def r(i,a): 
            if(a in d):
                if(d[a]!=0):
                    d[a]-=1
            if(i<=n-1):
                r(i+1,a+s[i])
                r(i+1,a)
        #l=[]
        n=len(s)
        d={}
        for i in words:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        k=d.copy()
        r(0,"")
        c=0
        #print(d)
        for i in k:
            if(d[i]!=k[i]):
                c=c+k[i]-d[i]
        return c"""