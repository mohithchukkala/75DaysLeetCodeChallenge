class Solution(object):
    def findDisappearedNumbers(self, nums):
        ans=[]
        arr=[0]*(len(nums))
        for i in nums:
            arr[i-1]=1
        for i in range(len(arr)):
            if arr[i]==0:
                ans.append(i+1)
        return ans
        