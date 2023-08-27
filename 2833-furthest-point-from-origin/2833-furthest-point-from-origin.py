class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=moves.count("L")
        r=moves.count("R")
        _=moves.count("_")
        return max(l,r)+_-min(l,r)