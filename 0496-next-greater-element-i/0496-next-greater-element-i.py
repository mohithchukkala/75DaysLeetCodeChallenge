class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        mp = {}

        # Find next greater for every element in nums2
        for num in nums2:

            while stack and num > stack[-1]:
                mp[stack.pop()] = num

            stack.append(num)

        # Remaining elements have no greater element
        while stack:
            mp[stack.pop()] = -1

        # Build answer for nums1
        ans = []

        for num in nums1:
            ans.append(mp[num])

        return ans