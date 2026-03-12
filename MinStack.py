class minStack():
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        
    def push(self,x):
        if len(self.min_stack)==0:
            self.min_stack.append(x)
        else:
            if x<=self.min_stack[-1]:
                self.min_stack.append(x)
        self.stack.append(x)
        
    def pop(self):
        if not self.stack:
            return 'Empty'
        elif self.stack[-1]==self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
    
    def top(self):
        if not self.stack:
            return 'Empty'
        return self.stack[-1]
    
    def getmin(self):
        if not self.stack:
            return 'Empty'
        return self.min_stack[-1]
    
answer=minStack()
answer.push(-2)
answer.push(0)
answer.push(-3)
print(answer.getmin())
print(answer.pop())
print(answer.top())
print(answer.getmin())
print(answer.min_stack)

