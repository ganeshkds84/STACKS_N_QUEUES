class Solution:
    def remove_k(self,num,k):
        stack=[]
        for digit in num:
            while stack and k>0 and digit<stack[-1]:
                stack.pop()
                k-=1
            stack.append(digit)
        
        while k>0:
            stack.pop()
            k-=1
        
        result=''.join(stack).lstrip('0')
        
        if result=='':
            return '0'
        
        return result
                
if __name__=='__main__':
    answr=Solution()
    num=input('Enter any number:')
    k=int(input('Enter within num length:'))
    print(answr.remove_k(num,k))
        