
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            fix the first num, find 2sum with 2 pointers
            if a match is found, slide until no duplicate
        '''
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            lp, rp = i + 1, len(nums) - 1
            while lp < rp:
                threesum = a + nums[lp] + nums[rp]
                if threesum > 0:
                    rp -= 1
                elif threesum < 0:
                    lp += 1
                else:
                    res.append([a, nums[lp], nums[rp]])
                    lp += 1
                    rp -= 1
                    while nums[lp] == nums[lp - 1] and lp < rp:
                        lp += 1
        return res