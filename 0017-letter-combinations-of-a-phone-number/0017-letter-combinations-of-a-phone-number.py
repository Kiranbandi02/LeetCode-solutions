class Solution:
    def letterCombinations(self, di: str) -> List[str]:
        from itertools import product
        d=[["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        if(len(di)==0):
            return []
        if(len(di)==1):
            return d[int(di)-2]
        l1=d[int(di[0])-2]
        for i in di[1:]:
            l2=d[int(i)-2]
            l1=list(product(l1,l2))
            o=[]
            for i1 in range(len(l1)):
                o.append(list(l1[i1][0])+list(l1[i1][1]))
            l1=o
        o=[]
        for i in l1:
            o.append("".join(i))
        return o
                