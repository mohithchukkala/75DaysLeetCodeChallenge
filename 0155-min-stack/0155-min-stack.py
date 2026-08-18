class MinStack(object):

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, value):
        self.stack1.append(value)

        if not self.stack2:
            self.stack2.append(value)
        else:
            self.stack2.append(min(self.stack2[-1],value))
        

    def pop(self):
        self.stack2.pop()
        return self.stack1.pop()
        

    def top(self):
        return self.stack1[-1]
        

    def getMin(self):
        return self.stack2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()