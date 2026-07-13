class Solution:
    def isHappy(self, n: int) -> bool:
        ap = set()
        while n not in ap:
            if n == 1:
                return True
            ap.add(n)
            n = sum(int(d)**2 for d in str(n))
        return False