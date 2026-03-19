class Solution:
    def subsum(self,nums):
        count=0
        n=len(nums)
        for i in range(n):
            min_ele=nums[i]
            for j in range(i,n):
                if nums[j]<min_ele:
                    min_ele=nums[j]
                count+=min_ele
                
        return count
    
if __name__=='__main__':
    answer=Solution()
    nums=list(map(int,input('Enter any numbers:').split()))
    print(answer.subsum(nums))
    