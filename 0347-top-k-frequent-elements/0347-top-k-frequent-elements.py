from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        dicti={}
        for i in nums:
            if i not in dicti:
                dicti[i]=1
            else:
                dicti[i]+=1
        new=sorted(dicti,key=lambda x:dicti[x],reverse=True)
        res=[]
        for i in range(k):
            res.append(new[i])
        return res
