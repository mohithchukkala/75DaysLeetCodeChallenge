class Solution(object):
    def findAnagrams(self, s, p):
        l=0
        ans=[]
        p_freq={}
        s_freq={}
        if len(p)>len(s):
            return []
        for i in range(len(p)):
            p_freq[p[i]]=p_freq.get(p[i],0)+1
        for i in range(len(p)):
            s_freq[s[i]]=s_freq.get(s[i],0)+1

        if s_freq==p_freq:
            ans.append(l)
        l+=1
        for i in range(len(p),len(s)):
            s_freq[s[l-1]]-=1
            if s_freq[s[l-1]]==0:
                del s_freq[s[l-1]]
            s_freq[s[i]]=s_freq.get(s[i],0)+1
            if s_freq==p_freq:
               ans.append(l)
            l+=1
        return ans