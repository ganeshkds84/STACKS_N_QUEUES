class Solution():
    def isVaild(self,string):
        stack=[]
        mapping={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for ch in string:
            if ch in mapping:
                if not stack:
                    return False
                if stack[-1]!=mapping[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)==0
    
    
a=input("Please select input from (){}[]:")
answer=Solution()
print(answer.isVaild(a))
