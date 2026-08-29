class Solution:
    def trap(self, height: List[int]) -> int:
        globalmax = 0
        indice = 0
        for i in range(len(height)):
            if globalmax <= height[i]:
                globalmax = height[i]
                indice = i

        solid = [0] * len(height)
        prefix = 0
        for i in range(indice+1):
            if height[i] > prefix:
                prefix = height[i]
            solid[i] = prefix
        
        suffix  = 0
        for i in range(len(height)-1,indice,-1):
            if height[i] > suffix:
                suffix = height[i]
            solid[i] = suffix
        
        ans = 0
        for i in range(len(solid)):
            if height[i] == solid[i]:
                continue
            ans += solid[i] - height[i]
        
        return ans
        

        