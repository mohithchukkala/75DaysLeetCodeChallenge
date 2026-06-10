class Solution(object):
    def merge(self, intervals):
        i=0
        res=[]
        intervals.sort(key=lambda x:x[0])
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            last=res[-1]
            if intervals[i][0]<=last[1]:
                last[1]=max(last[1],intervals[i][1])
                last[0]=min(last[0],intervals[i][0])
            else:
                res.append(intervals[i])
        return res
        
        

        