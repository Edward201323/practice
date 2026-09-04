class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = [[]]
        d = {}
        for i in range(0, len(nums)):
            d[nums[i]] = i
                
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                search = -(num[i] + num[j])
                if search in d and d[search] != i and d[search] != j:
                    sol.add([nums[i], nums[j], search])

        return sol