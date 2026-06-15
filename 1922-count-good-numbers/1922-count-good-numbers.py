
class Solution(object):
    def countGoodNumbers(self, n):
        mod=1000000007
        even_po=(n+1)//2
        odd_po=(n//2)

        res=(pow(5,even_po,mod)*pow(4,odd_po,mod))%mod
        return res