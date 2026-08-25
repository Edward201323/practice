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
            else:
                curr -= 1
            
            if blocks[i] == 'B':
                curr -= 1
            else:
                curr += 1

            minimum = min(minimum, curr)
                
        return minimum