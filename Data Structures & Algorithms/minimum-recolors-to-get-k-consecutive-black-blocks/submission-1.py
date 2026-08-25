class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimum = k
        for i in range(0, k):
            if blocks[i] == 'B':
                minimum -= 1
        
        curr = minimum
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'B':
                curr += 1
            if blocks[i - k] == 'W':
                curr -= 1

            if blocks[i] == 'B':
                curr -= 1
            if blocks[i] == 'W':
                curr += 1
        
        return minimum