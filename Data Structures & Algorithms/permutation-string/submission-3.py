class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1
        
        swCount = {}
        lp = 0
        for rp in range(len(s2)):
            
            if s2[rp] not in s1Count:
                lp = rp + 1
                swCount = {}
                continue
            else:
                swCount[s2[rp]] = swCount.get(s2[rp], 0) + 1
                while swCount[s2[rp]] > s1Count[s2[rp]]:
                    swCount[s2[lp]] -= 1
                    lp += 1
            if swCount == s1Count:
                return True
            
        return False