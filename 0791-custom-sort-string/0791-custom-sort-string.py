class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        c=0
        for i in order:
            d[i]=c
            c+=1
        l=[[] for j in range(len(order)+1)]
        for i in s:
            if(i in d):
                l[d[i]].append(i)
            else:
                l[-1].append(i)
        o=""
        for i in l:
            o+="".join(i)
        return o