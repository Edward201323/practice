class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        
        longest = 0
        for num in s:
            if num - 1 not in s:
                seq = 1
                while num + seq in s:
                    seq += 1
                
                if seq > longest:
                    longest = seq
        
        return longest