class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = tickets[k]
        for i in range(0, k):
            if tickets[i] < tickets[k]:
                time += tickets[i]
            else:
                time += tickets[k]
                
        for i in range(k + 1, len(tickets)):
            if tickets[i] < tickets[k]:
                time += tickets[i]
            else:
                time += tickets[k] - 1

        return time