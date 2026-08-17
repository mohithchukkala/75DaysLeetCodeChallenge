class Solution(object):
    def scoreOfParentheses(self, s):
        stack = []

        for i in s:
            if i == '(':
                stack.append(i)

            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    val = 0

                    while stack[-1] != '(':
                        val += stack.pop()

                    stack.pop()      
                    stack.append(2 * val)

        return sum(stack)