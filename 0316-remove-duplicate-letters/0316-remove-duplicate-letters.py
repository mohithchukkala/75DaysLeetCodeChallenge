class Solution(object):
    def removeDuplicateLetters(self, s):
        stack=[]
        last={}
        seen=set()
        for i,val in enumerate(s):
            last[val]=i
        for i,val in enumerate(s):
            if val in seen:
                continue
            while stack and stack[-1]>val and i<last[stack[-1]]:
                removed=stack.pop()
                seen.remove(removed)
            stack.append(val)
            seen.add(val)
        return ''.join(stack) 
        