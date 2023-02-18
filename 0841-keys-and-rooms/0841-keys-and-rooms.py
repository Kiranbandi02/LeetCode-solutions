class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        k=[0]*(len(rooms))
        a=[0]
        k[0]=1
        while(a!=[]):
            b=a.pop()
            for i in rooms[b]:
                if(k[i]==0):
                    k[i]=1
                    a.append(i)
        return all(k)