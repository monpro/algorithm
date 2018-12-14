class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        # for i in range(len(intervals)):
        #     for j in range(i+1, len(intervals)):
        #         if intervals[i].start > intervals[j].start:
        #             intervals[i], intervals[j] = intervals[j], intervals[i]
        intervals = sorted(intervals, key=lambda x: x.start)
        result = [intervals[0]]
        for i in intervals[1:]:
            if i.start <= result[-1].end:
                result[-1].end = max(i.end, result[-1].end)
            else:
                result.append(i)
        return result

        # new_intervals = []
        # i = 0
        # while i < len(intervals) - 1:
        #     if intervals[i] is None:
        #         i += 1
        #
        #
        #     for j in range(i + 1, len(intervals)):
        #         if intervals[j] is None:
        #             continue
        #         if intervals[i].end > intervals[j].start and intervals[i].end < intervals[j].end:
        #             intervals[i].end = intervals[j].end
        #             intervals[j] = None
        #             continue
        #         if intervals[i].end > intervals[j].end:
        #             intervals[j] = None
        #             continue
        #         if intervals[i].end == intervals[j].start:
        #             intervals[i].end = intervals[j].end
        #             intervals[j] = None
        #             continue
        #         if intervals[i].end < intervals[j].start:
        #             i += 1
        #             break
        # for i in intervals:
        #     if i is not None:
        #         new_intervals.append(i)
        # return new_intervals



l = Solution()

print(l.merge([[1,4],[4,5]]))


