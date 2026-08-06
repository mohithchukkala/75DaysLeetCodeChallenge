class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if matrix[i][0]<=target<=matrix[i][len(matrix[i])-1]:
                l=0
                r=len(matrix[i])-1

                while(l<=r):
                    mid=l+(r-l)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]>target:
                        r=mid-1
                    else:
                        l=mid+1
        return False
        