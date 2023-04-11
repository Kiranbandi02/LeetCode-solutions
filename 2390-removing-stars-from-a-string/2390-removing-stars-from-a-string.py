class Solution:
    def removeStars(self, s: str) -> str:
        s=list(s)
        k=[]
        for i in s:
            if(i!="*"):
                k.append(i)
            else:
                k.pop(-1)
        return "".join(k)