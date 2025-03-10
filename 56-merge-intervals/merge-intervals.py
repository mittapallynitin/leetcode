class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ranges = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for s, e in intervals:
            if ranges and ranges[-1][1] >= s:
                ranges[-1][1] = max(ranges[-1][1], e)
            else:
                ranges.append([s, e])
                
                
        return ranges
        