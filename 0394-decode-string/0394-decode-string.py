class Solution(object):
    def decodeString(self, s):
        stack=[]
        val=''
        for i in s:
            if i!=']':
                stack.append(i)
            else:
                new=''
                while stack[-1]!='[':
                    new=stack.pop()+new
                stack.pop()
                num=''
                while stack and stack[-1].isdigit():
                    num+=stack.pop()
                num=int(num[::-1])
                val=num*new
                stack.append(val)
        return ''.join(stack)
        