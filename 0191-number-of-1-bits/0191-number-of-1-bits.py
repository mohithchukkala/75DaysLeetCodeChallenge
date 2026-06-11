
def bin(s,n):
        while(n>=1):
            s=s+str(n%2)
            n=n//2
        return s.count('1')
class Solution(object):
    
    def hammingWeight(self, n):
        s=""
        ans=bin(s,n)
        return ans

        