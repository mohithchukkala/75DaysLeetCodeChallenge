class MyCircularDeque(object):

    def __init__(self, k):
        self.k=k
        self.d=deque()
        self.size=0
        

    def insertFront(self, value):
        if self.isFull():
            return False
        self.d.appendleft(value)
        self.size+=1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.d.append(value)
        self.size+=1
        return True
        

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.d.popleft()
        self.size-=1
        return True
        

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.d.pop()
        self.size-=1
        return True
        

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.d[0]
        

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.d[self.size-1]

        

    def isEmpty(self):
        return self.size==0
        

    def isFull(self):
        return self.size==self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()