class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            
            res = max(res, h * w)
            
            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]:
                r -= 1
        
        return res