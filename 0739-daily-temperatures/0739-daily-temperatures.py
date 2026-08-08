class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack=[]
        n=len(temperatures)
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while stack and stack[-1][0]<=temperatures[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1][1]-i
            else:
                ans[i]=0
            stack.append([temperatures[i],i])
        return ans 
        