class Solution(object):
    def rotate(self, nums, k):
        if k>len(nums):
            k=k%len(nums)
        def reverse(l,u):
            while(l<u):
                nums[l],nums[u]=nums[u],nums[l]
                l+=1
                u-=1
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)
        return nums
        