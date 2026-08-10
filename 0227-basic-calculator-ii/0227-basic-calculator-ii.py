class Solution(object):
    def calculate(self, s):
        stack=[]
        sign='+'
        num=0
        for i,ch in enumerate(s):
            if ch.isdigit():
                num=num*10+int(ch)
            if (not ch.isdigit() and ch!=' ') or i==len(s)-1:
                if sign=='+':
                    stack.append(num)
                elif sign=='-':
                    stack.append(-num)
                elif sign=='*':
                    stack.append(int(stack.pop()*num))
                elif sign=='/':
                    
                    a = stack.pop()
                    result = abs(a) // num

                    if a < 0:
                        result = -result

                    stack.append(result)
                sign=ch
                num=0
        return sum(stack)
        