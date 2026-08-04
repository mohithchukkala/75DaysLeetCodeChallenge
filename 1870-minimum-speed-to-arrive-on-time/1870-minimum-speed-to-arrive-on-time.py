class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        l=1
        r=10**7

        def cal(m):
            time=0
            for i in range(len(dist)):
                if i!=len(dist)-1:
                    time+=(dist[i]+m-1)//m
                else:
                    time+=float(dist[i])/m
            return time<=hour
        ans=-1
        while(l<=r):
            mid=l+(r-l)//2
            if cal(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
        