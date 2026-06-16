class Solution(object):
    def subsets(self, nums):
        res=[[]]
        def backtrack(start,num):
            for i in range(start,len(nums)):
                num.append(nums[i])
                res.append(num[:])
                backtrack(i+1,num)
                num.pop()

        backtrack(0,[])
        return res
        