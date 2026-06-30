class Solution(object):
    def maximumSubarraySum(self, nums, k):
        l=0
        freq={}
        tot,ans=0,0
        for i in range(len(nums)):
            tot+=nums[i]
            freq[nums[i]]=freq.get(nums[i],0)+1
            if i-l+1>k:
                freq[nums[l]]-=1
                tot-=nums[l]

                if freq[nums[l]]==0:
                    del freq[nums[l]]
                l+=1
            
            if i-l+1==k and len(freq)==k:
                ans=max(ans,tot)
        return ans