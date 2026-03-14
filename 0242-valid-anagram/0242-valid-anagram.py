from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        dict={}
        for i in s:
            dict[i]=dict.get(i,0)+1
        for i in t:
            if i not in dict:
                return False
            dict[i]-=1
        for i in dict:
            if dict[i]!=0:
                return False
        return True