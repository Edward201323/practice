"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# maximum amount of meetings overlapping at on emoment implies rooms needed
# use two sorted lists, one with start times and one with end times
# sorting seperately lets me sweep through times without caring which end belongs to which meetings
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted(interval.start for interval in intervals)
        end_times = sorted(interval.end for interval in intervals)
        
        # have a pointer at the start and end time, and keep count of the current rooms and max rooms
        """
        for each start time in sorted order:
            if the earliest remaining end time is at or before the start:
                a meeting has finished, so move the end pointer forward
            otherwise:
                no room is free, so we add a room
            update the highest room seen

        """

        end_index, current_rooms, max_rooms = 0, 0, 0

        for start in start_times:
            if end_times[end_index] <= start:
                end_index += 1 # a meeting has ended, so we reuse its room
            else:
                current_rooms += 1 # every room is in use, use a new room

            max_rooms = max(max_rooms, current_rooms)
        
        return max_rooms
            

