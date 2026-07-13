class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        bucket = [[] for _ in range(len(nums))]
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for num, freq in count.items():
            bucket[freq - 1].append(num)

        res = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                return res