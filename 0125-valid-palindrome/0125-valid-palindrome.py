class Solution(object):
    def isPalindrome(self, s):
        new=''
        for i in s:
            if i.isalpha() or i.isalnum():
                new+=i.lower()
        
        if new[:]==new[::-1]:
            return True
        else:
            return False        