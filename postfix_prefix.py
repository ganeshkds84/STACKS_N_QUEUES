from postfix_infix import postfix_infix
class postfix_prefix():
    def postfix(self,s):
        stack=[]
        for ch in s:
            if ch.isalnum():
                stack.append(ch)
            else:
                op1=stack.pop()
                op2=stack.pop()
                stack.append(ch+op2+op1)
                
        return stack.pop()
s=input("Enter any postfix expression:")    
if __name__=='__main__':
    obj=postfix_prefix()
    print(obj.postfix(s))
    