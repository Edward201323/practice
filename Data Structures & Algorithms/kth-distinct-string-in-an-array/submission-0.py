class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        uniques = set()
        duplicates = set()
        for num in arr:
            if num in uniques:
                uniques.remove(num)
                duplicates.add(num)

            if num not in uniques and num not in duplicates:
                uniques.add(num)

        uniques_counted = 0
        for num in arr:
            if num in uniques:
                uniques_counted += 1
            
            if uniques_counted == k:
                return num

        return ""