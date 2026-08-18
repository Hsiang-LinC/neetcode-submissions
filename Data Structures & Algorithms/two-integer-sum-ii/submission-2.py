class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1
        while rp > lp:
            sumTwo = numbers[lp] + numbers[rp]
            if sumTwo == target:
                return [lp + 1, rp + 1]
            elif sumTwo > target:
                rp -= 1
            elif sumTwo < target:
                lp += 1
