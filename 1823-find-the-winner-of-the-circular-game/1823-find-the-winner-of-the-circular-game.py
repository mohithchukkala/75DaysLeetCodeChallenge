class Solution(object):
    def findTheWinner(self, n, k):
        d=deque()
        ind=0
        for i in range(1,n+1):
            d.append(i)
        while len(d)!=1:
            ind=ind+k-1
            if ind>=len(d):
                ind=ind%len(d)
            d.remove(d[ind])
        return d.pop()


        