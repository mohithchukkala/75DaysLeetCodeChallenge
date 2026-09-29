class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        d=deque()
        t=0
        for i in range(len(tickets)):
            d.append((i,tickets[i]))
        while True:
            index,tickets=d.popleft()
            tickets-=1
            t+=1
            if index==k and tickets==0:
                return t
            if tickets>0:
                d.append((index,tickets))

        