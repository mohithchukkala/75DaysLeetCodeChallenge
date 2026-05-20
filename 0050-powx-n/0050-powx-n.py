import math
def pow(ans,n,x):
        if n==0:
            return ans
        elif n%2==0:
            x=x*x
            n=n//2
        else:
            ans=ans*x
            n=n-1
        return pow(ans,n,x)
class Solution(object):
    def myPow(self, x, n):
        ans=1
        if n==0:
            return 1
        if (n>0):
            return pow(ans,n,x)
        if (n<0):
            return 1/pow(ans,abs(n),x)

        