class Solution(object):
    def singleNonDuplicate(self, nums):
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
                return nums[mid]
            else:
                if mid%2==1:
                    mid-=1
                if nums[mid]==nums[mid+1]:
                    l=mid+2
                else:
                    r=mid
        return nums[l]
            

            

        