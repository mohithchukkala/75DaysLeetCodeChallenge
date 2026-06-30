class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l,o,r=0,0,0
        tot=0
        while(r<len(nums)):
            if nums[r]==1:
                r+=1
                o+=1
            else:
                tot=max(tot,o)
                o=0
                l+=1
                r=l
        tot=max(tot,o)
        return tot
            
        