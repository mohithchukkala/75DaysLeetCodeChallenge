class Solution(object):
    def moveZeroes(self, nums):
        l=0
        r=1
        if (len(nums)>1):
            while(r<len(nums)):
                if (nums[l]==0 and nums[r]!=0):
                    temp=nums[l]
                    nums[l]=nums[r]
                    nums[r]=temp
                    l+=1
                    r+=1
                elif nums[l]==0 and nums[r]==0:
                    r+=1
                else:
                    l+=1
                    r+=1
            return nums
        else:
            return nums



        
        