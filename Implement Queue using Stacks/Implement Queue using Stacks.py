class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.len = 0


    def push(self, x):
        self.stack1.append(x)
        self.len += 1
        return None


    def pop(self):
        if self.stack2:
            self.len -= 1
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                self.len -= 1
                return self.stack2.pop()
            else:
                raise Exception()


    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                return self.stack2[-1]
            else:
                raise Exception()


    def empty(self):
        return not bool(self.len)
