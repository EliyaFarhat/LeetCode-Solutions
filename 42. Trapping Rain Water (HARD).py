class Solution:
    def trap(self, height: List[int]) -> int:
        summ, minnl, maxl, minnr, maxxr = 0,0,0,0,0
        if len(set(height)) == 1:
            return 0
        for x in range(1,len(height)-1):
            if height[x-1] >= maxl:
                maxl = height[x-1]
            
            maxr = max(height[x::])
            minn = min(maxl, maxr)
            

            diff = minn - height[x]
            
            if diff >= 0:
                summ += diff
        return summ
