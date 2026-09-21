class Solution(object):
    def frequencySort(self, s):
        hash_map={}
        for i in s:
            hash_map[i]=hash_map.get(i,0)+1
        ans=""
        
        for char,freq in sorted(hash_map.items(),key=lambda x:x[1],reverse=True):
            ans+=char*freq
        return ans