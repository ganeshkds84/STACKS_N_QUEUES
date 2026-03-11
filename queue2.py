class stackQueue():
    
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def push(self,x):
        self.s1.append(x)
    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            return 'Empty'
        return self.s2.pop()
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            return 'Empty'
        return self.s2[-1]
    def isEmpty(self):
        return len(self.s1)==0 and len(self.s2)==0

obj=stackQueue()
obj.push(1)
obj.push(78)
obj.push(23)
print(obj.pop())
print(obj.peek())
print(obj.s1)
print(obj.s2)