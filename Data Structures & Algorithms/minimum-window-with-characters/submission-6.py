'''
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".
You may assume that the correct output is always unique.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
            lp to track start: reduce valid length
            rp to proceed: find matching
            move lp when match
            move rp when not match
            update res when length is shortened
        '''
        minLen = 100001
        res = ""
        lp, rp = 0, 0
        bestrp, bestlp = 0, 0
        sDict, tDict = {}, {}
        
        # contruct tDict
        for c in t:
            tDict[c] = tDict.get(c, 0) + 1
        
        # define matching criteria
        def isMatch(sDict, tDict):
            for c in tDict:
                if c not in sDict or sDict[c] < tDict[c]:
                    return False
            return True
        
        # sliding through s
        while rp < len(s):
            sDict[s[rp]] = sDict.get(s[rp], 0) + 1
            while isMatch(sDict, tDict):
                if rp - lp + 1 < minLen:
                    bestrp, bestlp = rp, lp
                    minLen = rp - lp + 1
                
                sDict[s[lp]] -= 1 
                lp += 1
            else:
                rp += 1
        return "" if minLen == 100001 else s[bestlp:bestrp+1]