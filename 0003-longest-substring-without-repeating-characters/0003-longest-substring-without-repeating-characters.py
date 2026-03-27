class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = []
        res = 0
        ans = 0

        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0

        for i in range(len(s)):
            if s[i] not in seen:
                seen.append(s[i])
                ans += 1
            else:
                res = max(res, ans)

                while s[i] in seen:
                    seen.pop(0)
                    ans -= 1

                seen.append(s[i])
                ans += 1

        return max(res, ans)