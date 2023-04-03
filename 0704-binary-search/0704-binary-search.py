class Solution:
    def search(self, a: List[int], target: int) -> int:
        def bi(l,h):
            if l<=h:
                m=(l+h)//2
                if(a[m]==target):
                    return m
                if(a[m]>target):
                    return bi(l,m-1)
                else:
                    return bi(m+1,h)
            else:
                return -1
        k=bi(0,len(a)-1)
        return k