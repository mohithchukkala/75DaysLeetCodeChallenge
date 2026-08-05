class Solution(object):
    def minDays(self, bloomDay, m, k):
        if len(bloomDay)<k*m:
            return -1
        ans=-1
        def can(mid):
            b=0
            f=0
            for bloom in bloomDay:
                if (bloom<=mid):
                    f+=1
                    if f==k:
                        b+=1
                        f=0
                else:
                    f=0
            return b>=m
        l=min(bloomDay)
        h=max(bloomDay)
        while(l<=h):
            mid=l+(h-l)//2
            if can(mid):
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans   