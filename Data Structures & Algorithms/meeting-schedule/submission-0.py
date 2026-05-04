"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort the meeting by start time, ascending
        for i in range(len(intervals)-1):
            for j in range(i, len(intervals)):
                if intervals[i].start>intervals[j].start:
                    intervals[i], intervals[j]=intervals[j], intervals[i]
        for i in range(len(intervals)-1):
            if intervals[i].end>intervals[i+1].start:
                return False


        return True