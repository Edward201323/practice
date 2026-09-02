class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sol = [-1] * 2
        curr = 0
        while curr < len(numbers):
            num = self.binarySearch(numbers, curr, target - numbers[curr])
            if num != -1:
                sol[0] = curr + 1
                sol[1] = num + 1
                return sol
            
            curr += 1

        return sol

    def binarySearch(self, numbers, left, target):
        right = len(numbers) - 1
        middle = left + right // 2
        while left <= right:
            curr = numbers[middle]
            if curr == target:
                return middle
            elif curr < target:
                left = curr + 1
            else:
                right = curr - 1

        return -1