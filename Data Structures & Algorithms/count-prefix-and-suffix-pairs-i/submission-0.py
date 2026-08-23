class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pairs = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                presuffix = words[i]
                curr = words[j]
                if i != j and curr.startswith(presuffix) and curr.endswith(presuffix):
                    pairs += 1

        return pairs