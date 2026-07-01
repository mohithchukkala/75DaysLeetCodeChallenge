class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k<=1: return 0
        p=1
        l=0
        count=0
        for i in range(len(nums)):
            p*=nums[i]
            while(p>=k):
                p/=nums[l]
                l+=1
            count+=i-l+1
        return count
            
            
            
        