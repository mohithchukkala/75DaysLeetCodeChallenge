class Solution(object):
    def searchMatrix(self, matrix, target):
        l,r=0,len(matrix[0])-1
        while (l>=0 and l<len(matrix)) and (r>=0 and r<=len(matrix[0])-1):
            if matrix[l][r]==target:
                return True
            elif matrix[l][r]>target:
                r-=1
            else:
                l+=1
        return False

                

        