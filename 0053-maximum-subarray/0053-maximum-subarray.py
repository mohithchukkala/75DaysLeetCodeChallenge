class Solution(object):
    def maxSubArray(self, nums):
        add=0
        max_sum=nums[0]
        for i in range(len(nums)):
            add+=nums[i]
            max_sum=max(max_sum,add)

            if add<0:
                add=0
        return max_sum
        