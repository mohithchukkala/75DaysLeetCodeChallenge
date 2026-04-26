class Solution(object):
    def longestCommonPrefix(self,strs):
      length_list=[len(i) for i in strs]
      L=min(length_list)
      
      while L>=0:
        count=0
        prefix=strs[0][0:L]
        for i in strs:
          l=i.startswith(prefix)
          if(l):
            count+=1
        if(count==len(strs)):
          return prefix
        L-=1