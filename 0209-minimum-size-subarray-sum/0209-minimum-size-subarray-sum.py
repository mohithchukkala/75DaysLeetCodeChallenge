class Solution(object):
    def minSubArrayLen(self, target, nums):
        add,l=0,0
        ans=float('inf')
        for i in range(len(nums)):
            add+=nums[i]
            while(add>=target):
                ans=min(ans,i-l+1)
                add-=nums[l]
                l+=1
        if ans==float('inf'):
            return 0
        else:
            return ans
                
        