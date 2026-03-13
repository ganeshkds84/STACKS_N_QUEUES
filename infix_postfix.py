class infixpostfix():
    def infix(self,string):
        postfix=''
        precedence={
            '+':1,'-':1,'*':2,'/':2,'^':3
        }
        stack=[]
        for ch in string:
            if ch.isalnum():
                postfix+=ch
            elif ch=='(':
                stack.append(ch)
            elif ch==')':
                while stack:
                    if stack[-1]=='(':
                        break
                    postfix+=stack.pop()
                stack.pop()
            else:
                while stack:
                    if stack[-1]=='(':
                        break
                    if precedence[ch]>precedence.get(stack[-1],0):
                        break
                    postfix+=stack.pop()
                stack.append(ch)
            
        while stack:
            postfix+=stack.pop()
            
        return postfix
    
obj=infixpostfix()
print(obj.infix('(a+b)*c'))
