class Solution:
    def subrange(self,nums):
        n=len(nums)
        pse=[-1]*n
        nse=[n]*n
        stack=[]
        
        for i in range(n):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if stack:
                pse[i]=stack[-1]
            else:
                pse[i]=-1
            stack.append(i)
            
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]>nums[i]:
                stack.pop()
            if stack:
                nse[i]=stack[-1]
            else:
                nse[i]=n
            stack.append(i)
            
        stack=[]
        nge=[-1]*n
        pge=[n]*n
        for i in range(n):
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            if stack:
                nge[i]=stack[-1]
            else:
                nge[i]=-1
            stack.append(i)
            
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]<nums[i]:
                stack.pop()
            if stack:
                pge[i]=stack[-1]
            else:
                pge[i]=n
            stack.append(i)
            
        min_sum=0
        max_sum=0
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            min_sum+=nums[i]*left*right
            left=i-nge[i]
            right=pge[i]-i
            max_sum+=nums[i]*left*right
            
        return max_sum-min_sum
    
if __name__=='__main__':
    answer=Solution()
    nums=list(map(int,input('Enter any numbers:').split()))
    print(answer.subrange(nums))
    