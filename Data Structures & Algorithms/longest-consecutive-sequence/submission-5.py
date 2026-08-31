class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            sequences = {}
            for num in nums:
                if num not in sequences:
                    sequences[num] = 1 + sequences.get(num - 1, 0) + sequences.get(num + 1, 0)
                    if num - 1 in sequences:
                        endpoint = num - sequences.get(num - 1)
                        sequences[endpoint] = sequences.get(num)
                    if num + 1 in sequences:
                        endpoint = num + sequences.get(num + 1)
                        sequences[endpoint] = sequences.get(num)

            highest = 0
            for num in sequences.values():
                if num > highest:
                    highest = num
            return highest