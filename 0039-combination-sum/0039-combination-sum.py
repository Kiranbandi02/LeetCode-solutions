class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        res=[]
        def d(i,l,t):
            if(t==target):
                res.append(l.copy())
                return
            if(i>=len(c) or t>target):
                return
            l.append(c[i])
            d(i,l,t+c[i])
            l.pop()
            d(i+1,l,t)
        d(0,[],0)
        return res