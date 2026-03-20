class Solution:
    def rectange(self,heights):
        
        stack=[]
        n=len(heights)
        pse=[-1]*n
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                pse[i]=stack[-1]
            else:
                pse[i]=-1
            stack.append(i)
            
        stack=[]
        nse=[n]*n
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                nse[i]=stack[-1]
            else:
                nse[i]=n
            stack.append(i)
            
            
        max_area=0
        for i in range(n):
            width=nse[i]-pse[i]-1
            area=heights[i]*width
            max_area=max(max_area,area)
            
        return max_area
    
if __name__=='__main__':
    answer=Solution()
    heights=list(map(int,input("Enter the heights:").split()))
    print(answer.rectange(heights))