class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if stack:
                    if i==')' and stack[-1]!='(':
                        return False
                    elif i==']' and stack[-1]!='[':
                        return False
                    elif i=='}' and stack[-1]!='{':
                        return False
                    stack.pop()
                else:
                    return False
                    
        if stack:
            return False
        else:
            return True
                
        