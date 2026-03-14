from postfix_infix import postfix_infix
class prefix_infix():
    def prefix(self,string):
        stack=[]
        string=string[::-1]
        for ch in string:
            if ch.isalnum():
                stack.append(ch)
            else:
                op1=stack.pop()
                op2=stack.pop()
                stack.append('('+op1+ch+op2+')')
        return stack[-1]
s=input("Enter any prefix expression:")
obj=postfix_infix()
print(obj.postfix(s[::-1]))
if __name__ == '__main__':
    answer=prefix_infix()
    print(answer.prefix(s))