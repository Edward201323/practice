class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key not in sol:
                sol[key] = []
            sol[key].append(s)

        result = []
        for value in sol.values():
            result.append(value)

        return result