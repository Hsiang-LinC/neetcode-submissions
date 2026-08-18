class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()
        lp, rp = 0, len(s) - 1
        while rp >= lp:
            if s[rp] != s[lp]:
                return False
            rp -= 1
            lp += 1
        return True