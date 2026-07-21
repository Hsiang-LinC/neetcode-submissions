class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            If sorted, we can check if next number is n+1, if so, add length, otherwise restart counting.
            But, sort takes nlogn.
            If we're just to check if next exist, use hashset.
            But to count the longest length, avoid search for both n-1 and n+1.
            Track the n-1. Can be done by simply checking if n-1 not in set, only then start checking n+1.  
        '''
        numSet = set(nums)
        maxLength = 0
        for n in nums:
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                maxLength = max(length, maxLength)
        
        return maxLength