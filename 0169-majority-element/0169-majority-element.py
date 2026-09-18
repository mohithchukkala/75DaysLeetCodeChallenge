class Solution(object):
    def majorityElement(self, nums):
        
        ele=0
        c=0
        for i in nums:
            if c==0:
                ele=i
            
            if i==ele:
                c+=1
            else:
                c-=1
        return ele