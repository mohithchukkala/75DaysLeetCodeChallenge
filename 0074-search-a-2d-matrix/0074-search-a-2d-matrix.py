class Solution(object):
    def searchMatrix(self, matrix, target):
        r=0
        for i in range(len(matrix)-1):
            if target>matrix[i][0] and target<matrix[i+1][0]:
                r=i
                break
            if target>matrix[len(matrix)-1][0]:
                r=len(matrix)-1
                break
            if matrix[i+1][0]==target or matrix[i][0]==target:
                return bool(1)
        j=0
        k=len(matrix[0])-1
        
        while j<=k:
            left=matrix[r][j]
            right=matrix[r][k]
            if target==left:
                return bool(1)
            elif target==right:
                return bool(1)
            else:
                j+=1
                k-=1
        return bool(0)
            

                
        