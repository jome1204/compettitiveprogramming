class MinStack(object):

    def __init__(self):
        self.stack = []


    def push(self, val):
        mini = val if not self.stack else min(self.stack[-1][1], val)
        self.stack.append([val, mini])



    def pop(self):
        self.stack.pop()



    def top(self):
        return self.stack[-1][0]



    def getMin(self):
        return self.stack[-1][1]
