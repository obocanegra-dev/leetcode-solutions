class Solution(object):
    def maxArea(self, height):
        n = len(height)
        left, right = 0, n - 1
        max_area = 0
        
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
