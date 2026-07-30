class Solution(object):
    def mySqrt(self, x):
        l=1
        r=x//2
        if x==1:
            return 1
        while(l<=r):
            mid=l+(r-l)//2
            s=(mid)*(mid)
            if s==x:
                return mid
            elif s<x:
                l=mid+1
            else:
                r=mid-1
        return r
                