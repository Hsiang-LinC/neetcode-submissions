class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        posDic = {}
        res = 0
        startPos = 0
        for i, c in enumerate(s):
            if c not in posDic:
                posDic[c] = i
            else:
                if posDic[c] >= startPos:
                    startPos = posDic[c] + 1
                posDic[c] = i
            res = max(res, i - startPos + 1)
        return res