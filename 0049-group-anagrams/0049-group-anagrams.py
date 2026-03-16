class Solution(object):
    def groupAnagrams(self, strs):
        dicti={}
        for i in strs:
            key=' '.join(sorted(i))
            if key not in dicti:
                dicti[key]=[]
            dicti[key].append(i)
        return dicti.values()
        