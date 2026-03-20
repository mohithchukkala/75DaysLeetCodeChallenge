class Solution(object):
    def removeDuplicates(self, nums):
        i,j=0,1
        while(i<j and j<len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
            j+=1
        return i+1