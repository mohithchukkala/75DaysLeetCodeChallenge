class Solution(object):
    def findMaxAverage(self, nums, k):
        l,r=0,k-1
        tot=0
        avg=0
        for i in range(l,r+1):
            tot+=nums[i]
        avg=float(tot)/k
        while(r<len(nums)-1):
            l+=1
            r+=1
            tot+=nums[r]-nums[l-1]
            avg=max(avg,float(tot)/k)
        return avg
            
        