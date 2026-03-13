from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        counter=Counter(nums)
        counter=sorted(counter.items(),key=lambda x:x[1],reverse=True)
        for element,freq in counter:
            if freq>1:
                return True
            else:
                return False

        