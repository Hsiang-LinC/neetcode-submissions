class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            every number could be candidate
            folyd's algorithm:
            sp, fp, where fp moves twice the speed of sp.
            sp and fp will meet in the cycle, where the distance to the entry will be the same as that from start to entry
        '''
        sp, fp = 0, 0
        while True:
            sp = nums[sp]
            fp = nums[nums[fp]]
            if sp == fp:
                break
        
        sp2 = 0
        while True:
            sp = nums[sp]
            sp2 = nums[sp2]
            if sp == sp2:
                return sp