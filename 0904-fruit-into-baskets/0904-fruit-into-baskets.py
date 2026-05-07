class Solution(object):
    def totalFruit(self, fruits):
        left=0
        t1=fruits[left]
        t2=float('inf')
        ans=0
        for right in range(1,len(fruits)):
            if fruits[right]==t1 or fruits[right]==t2:
                pass
            elif t2==float('inf'):
                t2=fruits[right]
            else:
                prev=fruits[right-1]
                left=right-1
                while prev==fruits[left]:
                    left-=1
                left+=1
                t1=fruits[left]
                t2=fruits[right]

            ans=max(right-left+1,ans)
        return 1 if len(fruits)==1 else ans
        