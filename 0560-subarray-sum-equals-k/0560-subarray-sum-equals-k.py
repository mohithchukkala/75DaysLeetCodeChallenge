class Solution(object):
    def subarraySum(self, nums, k):
        tot=0
        count=0
        freq={0:1}
        for i in range(len(nums)):
            tot+=nums[i]
            target=tot-k
            if target in freq:
                count+=freq.get(target,0)
            freq[tot]= freq.get(tot,0)+1
        return count