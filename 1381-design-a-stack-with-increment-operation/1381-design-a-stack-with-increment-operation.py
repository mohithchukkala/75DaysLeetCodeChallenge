class CustomStack(object):

    def __init__(self, maxSize):
        self.stack=[]
        self.stack1=[]
        self.s=maxSize
    def push(self, x):
        if len(self.stack)<self.s:
            self.stack.append(x)
        

    def pop(self):
        if len(self.stack)>=1:
            return self.stack.pop()
        else:
            return -1
        

    def increment(self, k, val):
        if len(self.stack)>k:
            while len(self.stack)!=k:
                self.stack1.append(self.stack.pop())
            while self.stack:
                self.stack1.append(self.stack.pop()+val)
            while self.stack1:
                self.stack.append(self.stack1.pop())
        else:
            while self.stack:
                self.stack1.append(self.stack.pop()+val)
            while self.stack1:
                self.stack.append(self.stack1.pop())
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)