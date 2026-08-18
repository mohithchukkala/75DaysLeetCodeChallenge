class Solution(object):
    def longestValidParentheses(self, s):
        stack=[-1]
        maxi=0
        for i,val in enumerate(s):
            if val=='(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    maxi=max(maxi,i-stack[-1])
                else:
                    stack.append(i)
        return maxi
        