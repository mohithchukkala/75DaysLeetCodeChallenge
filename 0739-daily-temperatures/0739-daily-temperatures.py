class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                previndex=stack.pop()
                ans[previndex]=i-previndex
            stack.append(i)
        return ans
            
                