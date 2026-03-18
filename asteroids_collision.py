class Solution:
    def collision(self,nums):
        stack=[]
        for i in range(len(nums)):
            alive=True
            while stack:
                if stack[-1]>0 and nums[i]<0:
                    if abs(nums[i])>stack[-1]:
                        stack.pop()
                    elif abs(nums[i])==stack[-1]:
                        stack.pop()
                        alive=False
                        break
                    else:
                        alive=False
                        break
                else:
                    break
            
            if alive:
                stack.append(nums[i])
                
        return stack
    
if __name__=='__main__':
    answer=Solution()
    nums=list(map(int,input('Enter the asteroids diameters:').split()))
    print(answer.collision(nums))
    
    