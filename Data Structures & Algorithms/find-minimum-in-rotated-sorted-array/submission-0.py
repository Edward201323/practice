class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[left] < nums[right]:
                right = middle
            else:
                left = middle
        
        return nums[left]
