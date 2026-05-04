class Solution(object):
    def sortColors(self, nums):
        low,high,mid=0,len(nums)-1,0
        while(mid<=high):
            if nums[mid]==0:
                temp=nums[mid]
                nums[mid]=nums[low]
                nums[low]=temp
                low=low+1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                temp=nums[mid]
                nums[mid]=nums[high]
                nums[high]=temp
                high-=1
        return nums
        