class Solution:
    def max_rectanle(self,matrix):
        m=len(matrix)
        n=len(matrix[0])
        max_area=0
        hist=[0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    hist[j]+=1
                else:
                    hist[j]=0
            stack=[]
            pse=[-1]*n
            nse=[n]*n
            for i in range(n):
                while stack and hist[stack[-1]]>=hist[i]:
                    stack.pop()
                if stack:
                    pse[i]=stack[-1]
                else:
                    pse[i]=-1
                stack.append(i)
                
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and hist[stack[-1]]>=hist[i]:
                    stack.pop()
                if stack:
                    nse[i]=stack[-1]
                else:
                    nse[i]=n
                stack.append(i)
                
            for i in range(n):
                width=nse[i]-pse[i]-1
                area=width*hist[i]
                max_area=max(area,max_area)
                
        return max_area
    
if __name__=='__main__':
    answer=Solution()
    matrix=[['1']]
    print(answer.max_rectanle(matrix))
    