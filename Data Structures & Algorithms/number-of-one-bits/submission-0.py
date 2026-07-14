class Solution:
    def hammingWeight(self, n: int) -> int:
        # Observation: n - 1 lead to the rightmost 1 to be 0
        # Additionally, the bits on the right side of that 1 will turn 1 as well
        # example: 010100 - 1 --> 101011
        # to keep the remaining 1s, use n & (n - 1)
        counts = 0
        while n:
            n &= (n - 1)
            counts += 1
        return counts