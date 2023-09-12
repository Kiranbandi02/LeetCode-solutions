class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter
        c=Counter(s)
        co=0
        se=set()
        for i in c:
            e,f=i,c[i]
            while f>0 and f in se:
                f-=1
                co+=1
            if(f>0):
                se.add(f)
        return co
            
        
        
        
        
        
        return c
                
                
                
                