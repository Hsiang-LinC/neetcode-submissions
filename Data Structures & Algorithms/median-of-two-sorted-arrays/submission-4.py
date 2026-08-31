class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
            obs:
                for median(s), the number of left and right group must have the same size.
                max of left group must not be larger than the min of the right group.
            Binary search on smaller array.
            Note: edge cases where all elements are in one group, or empty init arrays, we can set -inf and inf on the left and right most end.

            let mid be the close end of element we want to select in nums1
        '''
        # calculate the group size of left (and right).
        total_num = len(nums1) + len(nums2)
        n = total_num // 2 # for odd, exclude median; for even otherwise

        # search on the shorter array to avoid out of index on the other one
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        lp, rp = 0, len(nums1) - 1
        while True:
            m = (lp + rp) // 2
            # edge cases
            nums1Left = nums1[m] if m >= 0 else float('-inf')
            nums1Right = nums1[m+1] if m+1 <= len(nums1)-1 else float('inf')
            nums2Left = nums2[n-m-2] if n-m-2 >= 0 else float('-inf')
            nums2Right = nums2[n-m-1] if n-m-1 <= len(nums2)-1 else float('inf')

            if nums1Left > nums2Right:
                rp = m - 1
            elif nums2Left > nums1Right:
                lp = m + 1
            else:
                # if odd
                if total_num % 2:
                    return min(nums1Right, nums2Right)
                else:
                    return (min(nums1Right, nums2Right) + max(nums1Left, nums2Left)) / 2
            