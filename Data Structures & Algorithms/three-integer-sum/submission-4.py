class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        # -1, 0, 1, 2, -1, -4
        # -4, ,-1 ,-1, 0, 1, 2
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    sol.append([nums[i], nums[left], nums[right]])
                    break
        
        return sol