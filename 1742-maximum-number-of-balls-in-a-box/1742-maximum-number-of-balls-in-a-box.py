class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d={}
        n=highLimit-lowLimit+1
        for i in range(lowLimit,highLimit+1):
            s=0
            for j in str(i):
                s+=int(j)
            if(s not in d):
                d[s]=1
            else:
                d[s]+=1
        return max(d.values())