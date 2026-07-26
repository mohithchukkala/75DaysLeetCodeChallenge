class Solution(object):
    def maxAbsoluteSum(self, nums):
        maxi_sum=0
        mini_sum=0

        curr_max=0
        curr_mini=0
        for num in nums:
            curr_max=max(num,curr_max+num)
            maxi_sum=max(maxi_sum,curr_max)
        for num in nums:
            curr_mini=min(num,curr_mini+num)
            mini_sum=min(mini_sum,curr_mini)
        return max(maxi_sum,abs(mini_sum))
        