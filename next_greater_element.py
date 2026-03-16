class nextgreater():
    def nge(self,nums):
        n=len(nums)
        result=[-1]*n
        stack=[]
        for i in range(n):
            if not stack:
                stack.append(i)
            else:
                while stack:
                    if nums[i]>nums[stack[-1]]:
                        result[stack.pop()]=nums[i]
                    else:
                        break
                stack.append(i)
            
        
        return result
    
if __name__=='__main__':
    answer=nextgreater()
    a=list(map(int,input("Enter any numbers:").split()))
    print(answer.nge(a))