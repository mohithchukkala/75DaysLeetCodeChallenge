class Solution(object):
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            prev1 = 0
            prev2 = 0

            for num in arr:
                temp = prev1
                prev1 = max(prev1, prev2 + num)
                prev2 = temp

            return prev1

        return max(
            helper(nums[:-1]),  # exclude last
            helper(nums[1:])    # exclude first
        )