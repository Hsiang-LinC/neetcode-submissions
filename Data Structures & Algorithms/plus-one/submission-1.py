class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        proc = digits[-1] == 9
        d = -1
        while d >= -len(digits):
            if digits[d] == 9:
                digits[d] = 0
                d -= 1
            else:
                digits[d] += 1
                return digits
        if digits[0] == 0:
            digits.insert(0, 1)
            return digits