class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # conjecture: n + 1 integers in range (1,n)
        # implies there is at least one duplicate
        # implies other integer points to a non zero index

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
        return -1
        


            

