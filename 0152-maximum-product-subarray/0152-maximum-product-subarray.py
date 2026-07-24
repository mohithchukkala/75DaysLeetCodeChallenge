class Solution(object):
    def maxProduct(self, nums):
        pre,suff=1,1
        maxi_pre=nums[0]
        maxi_suff=nums[len(nums)-1]
        for i in range(len(nums)):
            pre*=nums[i]
            maxi_pre=max(maxi_pre,pre)
            if pre==0:
                pre=1
            
        for i in range(len(nums)-1,-1,-1):
            suff*=nums[i]
            maxi_suff=max(maxi_suff,suff)
            if suff==0:
                suff=1
        return max(maxi_pre,maxi_suff)
        
        return maxi
            
            
        