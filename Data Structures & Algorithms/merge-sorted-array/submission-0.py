class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''
            We merge the arrays backward, starting from the end of both arrays (m-1 from nums1)
            Two pointers
        '''
        p1, p2 = m - 1, n - 1

        for i in range(m + n - 1, -1, -1):
            if p1 == -1:
                nums1[i] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                if nums1[p1] <= nums2[p2]:
                    nums1[i] = nums2[p2]
                    p2 -= 1
                else:
                    nums1[i] = nums1[p1]
                    p1 -= 1
        return nums1