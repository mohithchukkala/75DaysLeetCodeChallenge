class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l=0
        tot=0
        for i in range(len(nums)):
            if nums[i]!=1:
                tot=max(tot,i-l)
                l=i+1
        tot=max(tot,i-l+1)
        return tot

        