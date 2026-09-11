class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = (len(heights) - 1) * min(heights[0], heights[-1])
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])

            if width * height > max_area:
                max_area = width * height

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

