class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        you can rob houses, but not two adjacent ones
        start from house 0, house 1 and make 2 different trees
        choose whether we want to skip two or three houses every ittereation
        
        return max of rob(0, nums) rob(1, nums)
        rob(int, nums):
            if int >= nums:
                return 0
            
            return nums[int] + max(rob(int + 2, nums), rob(int + 3), nums)
        
        
        """

        # memory = {}
        # def memoization(i, nums, memory):
        #     if i >= len(nums):
        #         return 0
            
        #     if i in memory:
        #         return memory[i]

        #     memory[i] = (nums[i] +
        #     max(memoization(i + 2, nums, memory), memoization(i + 3, nums, memory)))

        #     return memory[i]
        
        # return max(memoization(0, nums, memory), memoization(1, nums, memory))

        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2

        



        

        