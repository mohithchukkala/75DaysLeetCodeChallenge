class Solution(object):
    def twoSum(self, nums, target):
        nums=[(nums[i],i) for i in range(len(nums))]
        nums.sort()
        i=0
        j=len(nums)-1
        while(i<j):
            if nums[i][0]+nums[j][0]==target:
                return [nums[i][1],nums[j][1]]
            if nums[i][0]+nums[j][0]>target:
                j=j-1
            if nums[i][0]+nums[j][0]<target:
                i=i+1
        return None
        