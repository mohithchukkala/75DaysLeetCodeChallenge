class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        res = ""

        for i in range(len(s)):
            if i == 0 and (s[i] == '-' or s[i]=='+'):
                res += s[i]
                continue

            if s[i].isdigit():
                res += s[i]
            else:
                break

        if res == "" or res == "-" or res=="+":
            return 0
        res=int(res)

        if res < - (pow(2,31)):
            return -2147483648

        if res > pow(2,31) -1:
            return 2147483647


        return int(res)