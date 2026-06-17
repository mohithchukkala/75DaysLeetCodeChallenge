class Solution(object):
    def searchRange(self, nums, target):
        
        def first():
            l=0
            r=len(nums)-1
            ans=-1
            while(l<=r):
                mid=(l+r)//2
                if nums[mid]==target:
                    ans=mid
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return ans

        def last():
            l=0
            r=len(nums)-1
            ans=-1
            while(l<=r):
                mid=(l+r)//2
                if nums[mid]==target:
                    ans=mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return ans
        return [first(),last()]
        