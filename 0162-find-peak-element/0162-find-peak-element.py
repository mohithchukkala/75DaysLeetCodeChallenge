class Solution(object):
    def findPeakElement(self, nums):
        peak_ind=0
        if nums[len(nums)-1]>nums[len(nums)-2]:
                peak_ind=len(nums)-1
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i] and nums[i+1]<nums[i]:
                peak_ind=i
            if nums[len(nums)-1]>nums[len(nums)-2]:
                peak_ind=len(nums)-1
        return peak_ind
            
