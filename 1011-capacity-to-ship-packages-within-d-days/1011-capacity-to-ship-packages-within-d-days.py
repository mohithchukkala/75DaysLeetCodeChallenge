class Solution(object):
    def shipWithinDays(self, weights, days):
       
        def cap(w):
            add,day=0,1
            for i in weights:
                if add+i<=w:
                    add+=i
                else:
                    add=i
                    day+=1

            
            return day<=days
        low=max(weights)
        high=sum(weights)
        ans=0
        while(low<=high):
            mid=low+(high-low)//2
            if cap(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        