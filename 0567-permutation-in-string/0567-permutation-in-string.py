class Solution(object):
    def checkInclusion(self, s1, s2):
        s1_freq={}
        s2_freq={}
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            s1_freq[s1[i]]=s1_freq.get(s1[i],0)+1
        l=0
        for i in range(len(s1)):
            s2_freq[s2[i]]=s2_freq.get(s2[i],0)+1
        if s2_freq==s1_freq:
            return True
        l+=1

        for i in range(len(s1),len(s2)):
            s2_freq[s2[l-1]]-=1
            if s2_freq[s2[l-1]]==0:
                del s2_freq[s2[l-1]]
            s2_freq[s2[i]]=s2_freq.get(s2[i],0)+1
            if s2_freq==s1_freq:
                return True
            l+=1
        return False

        