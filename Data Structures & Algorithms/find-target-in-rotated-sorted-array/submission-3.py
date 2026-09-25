class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums is sorted, then rotated n times
        # I for sure have to use binary search with some sort of altered algorithm
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            # first check to see if this is correct
            if nums[middle] == target:
                return middle
            # ordinary binary search nums[left] < nums[right] because we're essnetially searching in a non rotated array
            elif nums[left] < nums[right]:
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            # num[left] < num[middle] implies left half is sorted
            elif nums[left] <= nums[middle]:
                if nums[left] <= target and target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

            # num[middle] < num[right] implies that the second half is sorted
            else:
                if nums[middle] <= target and target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1


        # 3 4 5 6 1 2, target = 1
        # one half of our array, will always be sorted
        # to solve, we should first find the half that is sorted
        # if the half is sorted, and the target resides between the range, shrink the search size to that half
        # if its not, we should search inside of the other half