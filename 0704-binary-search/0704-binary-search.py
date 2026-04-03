class Solution(object):
    def search(self, nums, target):
        i=0
        j=len(nums)-1
        if len(nums)==1:
            if target==nums[0]:
                return 0
        while(i<=j):
            mid=(i+j)/2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                i=mid+1
            else:
                j=mid-1
        return -1
        