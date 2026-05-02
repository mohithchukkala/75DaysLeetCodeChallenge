class Solution(object):
    def reverseString(self,s):
        for i in range(len(s)//2):
            v=s[len(s)-i-1]
            s[len(s)-i-1]=s[i]
            s[i]=v
        return s
        