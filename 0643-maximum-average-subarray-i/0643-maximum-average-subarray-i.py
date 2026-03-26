class Solution(object):
    def findMaxAverage(self, nums, k):
        if len(nums)==1:
            return nums[0]
        res=sum(nums[:k])
        mres=res
        l=1
        r=k
        while(r<len(nums)):
            res+=nums[r]
            res-=nums[l-1]
            mres=max(res,mres)
            l+=1
            r+=1
        return float(mres)/k


        
        