class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack=[]
        ans=list(s)

        for i,val in enumerate(s):
            if val=='(':
                stack.append(i)
            elif val==')':
                if stack:
                    stack.pop()
                else:
                    ans[i]=''
        while stack:
            ans[stack.pop()]=''
        return ''.join(ans)
        