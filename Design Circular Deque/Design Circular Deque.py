class MyCircularDeque(object):

    def __init__(self, k):
        self.k = k
        self.arr = []
        
        

    def insertFront(self, value):
        if self.isFull():
            return False
        else:
            self.arr.insert(0,value)      
            return True        
       
        

    def insertLast(self, value):
        if len(self.arr) >= self.k:
            return False
        else:
            self.arr.append(value)
            return True
        
        

    def deleteFront(self):
        if self.isEmpty():
            return False
        else:
            del  self.arr[0]
            return True


    def deleteLast(self):
        if self.isEmpty():
            return False
        else:
            del self.arr[-1]
            return True
        

    def getFront(self):
        if not self.isEmpty(): 
            return self.arr[0]
        else:
            return -1     

        

    def getRear(self):
        if not self.isEmpty():
            return self.arr[-1]
        else:
            return -1

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False
        

    def isFull(self):
         return len(self.arr) == self.k
