class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for number, occurences in d.items():
            freq[occurences].append(number)
        
        sol = []
        for arr in reversed(freq):
            for num in arr:
                sol.append(num)
                if len(sol) == k:
                    return sol

        return sol