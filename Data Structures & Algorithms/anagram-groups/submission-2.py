class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = {}
        for s in strs:
            count = Counter(s)
            key = frozenset(count.items())
            if key not in sol:
                sol[key] = [] 
            sol[key].append(s)

        result = []
        for value in sol.values():
            result.append(value)
        
        return result