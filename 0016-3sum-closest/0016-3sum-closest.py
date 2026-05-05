class Solution(object):
    def threeSumClosest(self, nums, target):
        n=len(nums)
        nums.sort()
        ans=float('inf')
        for i in range(n-2):
            left=i+1
            right=n-1

            while(left<right):
                z=nums[i]+nums[left]+nums[right]
                if abs(target-z)<abs(target-ans):
                    ans=z
                if z<target:
                    left+=1
                elif z>target:
                    right-=1
                else:
                    return z
        return ans


        