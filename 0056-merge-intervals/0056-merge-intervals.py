class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l=[]
        intervals.sort()
        for i in intervals:
            if(len(l)==0 or l[-1][1]<i[0]):
                l.append(i)
            else:
                l[-1][1]=max(l[-1][1],i[1])
        return l