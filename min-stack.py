# the idea here is to use extra space trading off the time
# use an extra minStack to keep track of the smallest num
class MinStack:
    def __init__(self):
        self.Stack = []
        self.minStack = []
    
    def push(self, x):
        self.Stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:   # <=, not <, if you consider duplicates
            self.minStack.append(x)
    
    def pop(self):
        if self.Stack.pop() == self.minStack[-1]:
            self.minStack.pop()
    
    def top(self):
        return self.Stack[-1]

    def getMin(self):
        return self.minStack[-1]
