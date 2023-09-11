class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if(nums==[]):
            return []
        t=[[nums[0]]]
        for i in nums[1:]:
            if(i==t[-1][-1]+1):
                t[-1].append(i)
            else:
                t.append([i])
        l=[]
        for i in t:
            if(len(i)!=1):
                l.append("{}->{}".format(i[0],i[-1]))
            else:
                l.append("{}".format(i[0]))
        return l
                