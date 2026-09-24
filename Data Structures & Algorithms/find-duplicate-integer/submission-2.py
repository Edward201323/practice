class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow_index = slow % len(nums)
            fast_index = fast % len(nums)
            if slow_index != fast_index and nums[slow_index] == nums[fast_index]:
                return nums[slow_index]

            slow += 1
            fast += 2
        
        return -1
