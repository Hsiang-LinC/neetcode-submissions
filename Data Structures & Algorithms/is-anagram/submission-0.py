class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # abcd, dbca
        # use dict, hash table to accumulate the count

        cc = {}
        for c in s:
            if c not in cc:
                cc[c] = 1
            else:
                cc[c] += 1
        for c in t:
            if c not in cc or cc[c] <= 0:
                return False
            else:
                cc[c] -= 1
        if all(v == 0 for v in cc.values()):
            return True
        else:
            return False