class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
    
        def roberI(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                temp = rob2
                rob2 = max(rob1 + num, rob2)
                rob1 = temp
            
            return rob2

        return max(roberI(nums[1:]), roberI(nums[:-1]))
        



        

        