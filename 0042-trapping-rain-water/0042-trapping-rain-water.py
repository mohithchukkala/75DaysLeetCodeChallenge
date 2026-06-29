class Solution(object):
    def trap(self, height):
        l,w=0,0
        r=len(height)-1
        lm,rm=height[l],height[r]
        while l<r:
            if lm<=rm:
                l+=1
                lm=max(lm,height[l])
                w+=lm-height[l]
            else:
                r-=1
                rm=max(rm,height[r])
                w+=rm-height[r]
        return w
        