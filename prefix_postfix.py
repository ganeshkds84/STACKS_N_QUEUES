#from prefix_infix import prefix_infix
#from infix_postfix import infixpostfix

#obj=prefix_infix()
#s=obj.prefix('+ab')
#obj2=infixpostfix()
#print(obj2.infix(s))

class prefix_postfix():
    def prefix(self,s):
        stack=[]
        s=s[::-1]
        for ch in s:
            if ch.isalnum():
                stack.append(ch)
            else:
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op1+op2+ch)
        return stack.pop()
    
if __name__=='__main__':
    s=input("Enter the prefix expression:")
    raju=prefix_postfix()
    print(raju.prefix(s))
    