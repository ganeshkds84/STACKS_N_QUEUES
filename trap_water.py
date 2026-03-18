class Solution():
    def trap(self,height):
        n=len(height)
        lefty=[0]*n
        righty=[0]*n
        lefty[0]=height[0]
        righty[-1]=height[-1]
        for i in range(1,n):
            lefty[i]=max(lefty[i-1],height[i])
            righty[n-i-1]=max(righty[n-i],height[n-i-1])
        result=[]
        for i in range(n):
            req=min(lefty[i],righty[i])-height[i]
            result.append(req)
            
        return sum(result)
if __name__=='__main__':
    height=list(map(int,input('Enter the heights:').split()))
    answer=Solution()
    print(answer.trap(height))
    
