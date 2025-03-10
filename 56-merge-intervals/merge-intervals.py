class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ranges = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for s, e in intervals:
            if not ranges or ranges[-1][1] < s:
                ranges.append([s, e])
            else:
                ranges[-1][1] = max(ranges[-1][1], e)
                
        return ranges
        