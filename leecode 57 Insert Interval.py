__author__ = 'YE'

__author__ = 'YE'

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x.start)

        length = len(intervals)
        res = []

        if length == 0:
            res.append(newInterval)
            return res

        res.append(intervals[0])
        for i in range(1,length):
            size = len(res)
            if res[size - 1].start <= intervals[i].start <= res[size - 1].end:
                res[size - 1].end = max(intervals[i].end, res[size - 1].end)
            else:
                res.append(intervals[i])

        return res
