class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # this problem can easily be solved using a set
        # itterate through ll, store the current node's value
        # if the current value has been used, retunr the number
        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)

        return -1