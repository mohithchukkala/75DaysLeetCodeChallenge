class Solution(object):
    def checkSubarraySum(self, nums, k):
        hm={0:-1}
        tot=0
        for i in range(len(nums)):
            tot+=nums[i]
            per=tot%k
            if per in hm:
                if i-hm[per]>=2:
                    return True
            else:
                hm[per]=i
        return False


        