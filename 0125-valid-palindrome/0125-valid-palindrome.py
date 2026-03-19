class Solution(object):
    def isPalindrome(self, s):
        new=''
        for i in s:
            if i.isalnum():
                new+=i
        new=new.lower()
        if new[:]!=new[::-1]:
            return False
        return True
        
        
        
        