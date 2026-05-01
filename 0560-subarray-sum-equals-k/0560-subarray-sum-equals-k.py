class Solution(object):
    def subarraySum(self, nums, k):
        presum=0
        count=0
        freq={}
        freq[0]=1
        for i in nums:
            presum+=i
            v=presum-k
            if v in freq:
                count+=freq[v]
            if presum not in freq:
                freq[presum]=1
            else:
                freq[presum]+=1
        return count         