class Solution(object):
    def makeGood(self, s):
        stack=[]
        for i in s:
            if stack:
                if stack[-1].lower()==i.lower() and stack[-1]!=i:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        print(stack)
        return ''.join(stack)

        