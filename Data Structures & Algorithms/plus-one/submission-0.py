class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        proc = digits[-1] == 9
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                proc = False
                return digits
        if proc:
            digits.insert(0, 1)
            return digits