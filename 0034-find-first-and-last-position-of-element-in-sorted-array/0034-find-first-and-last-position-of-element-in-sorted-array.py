class Solution(object):
    def searchRange(self, nums, target):
        
        def first():
            l=0
            r=len(nums)-1
            ans=-1
            while(l<=r):
                mid=l+(r-l)//2
                if nums[mid]==target:
                    r=mid-1
                    ans=mid
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return ans
        def last():
            l=0
            r=len(nums)-1
            ans=-1
            while(l<=r):
                mid=l+(r-l)//2
                
                if nums[mid]==target:
                    l=mid+1
                    ans=mid
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return ans
        return [first(),last()]
        