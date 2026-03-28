class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        maxcount = 0
        res = 1
        freq = {}

        while(right < len(s)):
            if(s[right] in freq):
                freq[s[right]] = freq[s[right]] + 1
            else:
                freq[s[right]] = 1
            
            maxcount = max(maxcount , freq[s[right]])
            if(abs( maxcount - (right - left + 1)) > k):
                freq[s[left]] -= 1
                left +=  1

            res = max(res , right-left+1)
            right += 1
        
        return res