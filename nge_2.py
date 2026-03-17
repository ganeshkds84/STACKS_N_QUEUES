class Solution():
    def nge(self,nums):
        n=len(nums)
        result=[-1]*n
        stack=[]
        for i in range(2*n):
            while stack:
                if nums[i%n]>nums[stack[-1]]:
                    result[stack.pop()]=nums[i%n]
                else:
                    break
            if i<n:
                stack.append(i)
        
        return result
if __name__=='__main__'    :
    answer=Solution()
    nums=list(map(int,input("Enter any numbers:").split()))
    print(answer.nge(nums))
