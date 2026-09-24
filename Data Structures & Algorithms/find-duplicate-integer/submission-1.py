class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # another solution is sorting then using 2 ptrs
        nums.sort()
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                return nums[left]
            left += 1
            right += 1
        
        return -1