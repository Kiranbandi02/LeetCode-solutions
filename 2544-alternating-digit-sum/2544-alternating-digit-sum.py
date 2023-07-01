class Solution:
    def alternateDigitSum(self, n1: int) -> int:
        p=[]
        n=[]
        f=1
        for i in str(n1):
            if(f==1):
                p.append(int(i))
                f=0
            else:
                n.append(int(i))
                f=1
        return sum(p)-sum(n)
            