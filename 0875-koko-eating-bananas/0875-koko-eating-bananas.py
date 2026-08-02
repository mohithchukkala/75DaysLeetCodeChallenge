class Solution(object):
    def minEatingSpeed(self, piles, h):
        l=1
        r=max(piles)
        ans=-1
        while(l<=r):
            mid=l+(r-l)//2
            hours=0
            for i in range(len(piles)):
                hours+=(piles[i]+mid-1)//mid
            if hours<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
            