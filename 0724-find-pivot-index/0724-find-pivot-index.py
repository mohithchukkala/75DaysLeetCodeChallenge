class Solution(object):
    def pivotIndex(self, nums):
        tot,p_s=0,0
        for i in range(len(nums)):
            tot+=nums[i]
        for i in range(len(nums)):
            p_s+=nums[i]
            if p_s-nums[i]==tot-p_s:
                return i
        else:
            return -1