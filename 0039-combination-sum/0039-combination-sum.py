class Solution(object):
    def combinationSum(self, candidates, target):
        res=[]
        def backtrack(j,target,num):
            if target==0:
                res.append(num[:])
                return
            if target<0:
                return 
            for i in range(j,len(candidates)):
                num.append(candidates[i])
                backtrack(i,target-candidates[i],num)
                num.pop()
        backtrack(0,target,[])
        return res
        