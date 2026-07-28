class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        maxi=1
        freq={}
        if (s==""):
            return 0
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
            
            if freq[s[i]]>1:
                while(freq[s[i]]>1):
                    freq[s[l]]-=1
                    if freq[s[l]]==0:
                        del freq[s[l]]
                    l+=1
            maxi=max(maxi,i-l+1)
        return maxi

        