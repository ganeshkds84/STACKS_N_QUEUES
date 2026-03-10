class Stack():
    def __init__(self):
        self.stack=[]
        
    def push(self,x):
        return self.stack.append(x)
    
    def pop(self):
        if not self.stack:
            return 'Stack is empty'
        return self.stack.pop()
        
    def top(self):
        if not self.stack:
            return 'Stack is empty'
        return self.stack[-1]
    
    def isEmpty(self):
        return self.stack==[]
    
s1=Stack()
s1.push(30)
s1.push(20)
print(s1.pop())
print(s1.stack)
print(s1.top())
s1.pop()
s1.push(25)
print(s1.isEmpty())
print(s1.stack)