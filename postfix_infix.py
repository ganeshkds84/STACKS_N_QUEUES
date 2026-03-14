class postfix_infix():
    def postfix(self,string):
        stack=[]
        for ch in string:
            if ch.isalnum():
                stack.append(ch)
            else:
                op2=stack.pop()
                op1=stack.pop()
                stack.append('('+op1+ch+op2+')')
        return stack[-1]
    
obj=postfix_infix()
print(obj.postfix('abc*+'))
                