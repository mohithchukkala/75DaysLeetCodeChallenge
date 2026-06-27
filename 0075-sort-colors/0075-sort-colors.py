class Solution(object):
    def sortColors(self, nums):
        l=0
        mid=0
        r=len(nums)-1
        while(mid<=r):
            if nums[mid]==2:
                temp=nums[mid]
                nums[mid]=nums[r]
                nums[r]=temp
                
                r-=1
            elif nums[mid]==1:
                temp=nums[mid]
                nums[mid]=nums[l]
                nums[l]=temp

                mid+=1
            else:
                temp=nums[l]
                nums[l]=nums[mid]
                nums[mid]=temp

                l+=1
                mid+=1
        

        return nums


            

        