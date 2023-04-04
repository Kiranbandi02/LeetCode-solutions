class Solution:
    def partitionString(self, s: str) -> int:
        k=[]
        a=""
        for i in s:
            if(i not in a):
                a=a+i
            else:
                k.append(a)
                a=i
        k.append(a)
        return len(k)