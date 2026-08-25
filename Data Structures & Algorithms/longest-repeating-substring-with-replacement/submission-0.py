class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            1. Do not track each char length or breakpoint separately, this would requires O(n^2).
            2. Track max substring length and max single char counts in any sliding window so far.
            3. Note, we do not need to reduce such max single char counts, since it would be updated when max substring length is updated, as the contraint must hold:
            max substring length - max single char counts <= k
        '''
        res = 0
        maxf = 0
        countDict: dict[str, int] = {}
        lp = 0

        for rp in range(len(s)):
            countDict[s[rp]] = countDict.get(s[rp], 0) + 1
            maxf = max(maxf, countDict[s[rp]])
            length = rp - lp + 1
            
            while length - maxf > k:
                countDict[s[lp]] -= 1
                length -= 1
                lp += 1
            
            res = max(res, rp - lp + 1)
        return res
                
                    