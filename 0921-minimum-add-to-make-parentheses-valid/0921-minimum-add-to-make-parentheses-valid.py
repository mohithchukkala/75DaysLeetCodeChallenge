class Solution(object):
    def minAddToMakeValid(self, s):
        o,c=0,0
        for i in s:
            if i=='(':
                o+=1
            else:
                if i==')' and o>0:
                     o-=1
                else:
                    c+=1
        if c>0 and o>0:
            ans=c+o
            return ans
        else:
            return max(o,c)
            
        