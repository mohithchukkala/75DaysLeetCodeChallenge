class Solution(object):
    def totalFruit(self, fruits):
        l,ans=0,0
        freq={}
        for i in range(len(fruits)):
            freq[fruits[i]]=freq.get(fruits[i],0)+1

            while len(freq)>2:
                freq[fruits[l]]-=1
                if freq[fruits[l]]==0:
                    del freq[fruits[l]]
                l+=1

            ans=max(ans,i-l+1)
        return ans