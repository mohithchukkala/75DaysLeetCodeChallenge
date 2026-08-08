class Solution(object):
    def asteroidCollision(self, asteroids):
        stack=[]
        for i in range(len(asteroids)):
            stack.append(asteroids[i])
            while len(stack)>1 and stack[-1]<0:
                if (stack[-1]<0 and stack[-2]>0) or (stack[-1]>0 and stack[-2]<0):
                    if abs(stack[-1])==abs(stack[-2]):
                        stack.pop()
                        stack.pop()
                    elif abs(stack[-1])<abs(stack[-2]):
                        stack.pop()
                    else:
                        a=stack.pop()
                        stack.pop()
                        stack.append(a)
                
                else:
                    break
        
        return stack
            
        

            