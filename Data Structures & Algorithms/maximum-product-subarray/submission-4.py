class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # keep track to max_prod to return
        # start cur_prod from 1
        # track prod up until the first neg
        # track prod from the last neg, reset when 0 or next neg is met
        # if 0 is met, reset cur_prod to 1
        max_prod = nums[0]
        cur_prod = 1
        prod_first_neg = 0
        prod_last_neg = 1
        neg_count = 0
        for i in range(len(nums)):
            cur_prod *= nums[i]
            prod_last_neg *= nums[i]
            max_prod = max(max_prod, cur_prod)
            if nums[i] < 0:
                neg_count += 1
                if neg_count == 1:
                    prod_first_neg = cur_prod
                prod_last_neg = nums[i]
            elif nums[i] == 0 or i == len(nums) - 1:
                if cur_prod < 0 and neg_count % 2 == 1:
                    div = max(prod_first_neg, prod_last_neg)
                    cur_prod //= div
                    max_prod = max(cur_prod, max_prod)
                cur_prod = 1
                prod_first_neg = 1
                prod_last_neg = 0
                neg_count = 0
        return max_prod