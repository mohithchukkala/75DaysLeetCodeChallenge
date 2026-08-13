class Solution(object):
    def minLength(self, s):
        stack=[]
        for i in range(len(s)):
            if stack and stack[-1] in 'AC':
                if s[i] in 'BD':
                    if ord(s[i])==ord(stack[-1])+1:
                        stack.pop()
                    else:
                        stack.append(s[i])
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return len(stack)

        