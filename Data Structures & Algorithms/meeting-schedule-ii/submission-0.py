"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# 0 ->                         40
# 5 -> 10
#         15 -> 20

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals_sorted = [(i.start, i.end) for i in intervals]
        intervals_sorted.sort()
        
        sol = 0
        rooms = []
        for interval in intervals_sorted:
            # while true: if interval not in top of the stack, pop
            # append interval to the top of the stack
            while rooms and interval[0] > rooms[-1][1]:
                rooms.pop()
            rooms.append(interval)
            sol = max(sol, len(rooms))
            
        return sol



