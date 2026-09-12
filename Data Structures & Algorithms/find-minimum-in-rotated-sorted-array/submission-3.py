class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            right_middle = (left + right) // 2
            left_middle = right_middle - 1
            min_index = nums.index(min(nums[left], nums[left_middle],
            nums[right_middle], nums[right]))
            if min_index <= left_middle:
                right = left_middle
            else:
                left = right_middle

        
        return min(nums[left], nums[right])
            