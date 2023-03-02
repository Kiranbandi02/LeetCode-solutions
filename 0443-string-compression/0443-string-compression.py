class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        res=0
        while i<len(chars):
            g=1
            while(i+g<len(chars) and chars[i+g]==chars[i]):
                g+=1
            chars[res]=chars[i]
            res+=1
            if g>1:
                chars[res:res+len(str(g))]=list(str(g))
                res+=len(str(g))
            i+=g
            
        return res
            
        