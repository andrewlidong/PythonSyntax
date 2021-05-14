'''
15. Merge overlapping intervals

Given a collection of intervals, merge all overlapping intervals. See the example below.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Solution: 

This problem can be solved utilizing a simple linear search algorithm, since we already know that inputs are sorted by starting timestamps. Here’s the approach we will take:

List of input intervals is given, and we’ll keep merged intervals in the output list.
For each interval,

If the input interval is overlapping with the last interval in the output list, we’ll merge the two intervals and update the last interval of the output list with the merged interval.

Otherwise, we’ll add an input interval to the output list.


Time: O(N)
Space: O(N)
'''

from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    if len(intervals) < 2:
        return intervals

    # sort intervals on start time
    intervals.sort(key=lambda x: x.start)

    mergedIntervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        # overlapping intervals, adjust end
        if interval.start <= end:
            end = max(interval.end, end)
        # nonoverlapping interval, simply append
        else:
            mergedIntervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    # add last interval
    mergedIntervals.append(Interval(start, end))
    return mergedIntervals


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
