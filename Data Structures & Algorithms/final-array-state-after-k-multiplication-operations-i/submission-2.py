class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))

        heapq.heapify(arr)
        while k > 0:
            new_value, i = heapq.heappop(arr)
            heapq.heappush(arr, (new_value * multiplier, i))
            k -= 1

        result = [0] * len(nums)
        for value, i in arr:
            result[i] = value
        
        return result
        