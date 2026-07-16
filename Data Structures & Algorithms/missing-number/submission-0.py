class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
            Observation:
                add up, compare to the sum w/o the absence
        '''
        n = len(nums)
        sum_full = n * (n + 1) // 2
        sum_nums = 0
        for i in range(n):
            sum_nums += nums[i]
        
        return sum_full - sum_nums