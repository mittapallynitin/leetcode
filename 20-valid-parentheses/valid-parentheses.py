class Solution:
    def isValid(self, s: str) -> bool:
        complement = {
            "(" : ")", 
            "{" : "}",
            "[" : "]"
        }

        tracker = []

        for ch in s:
            if tracker and complement.get(tracker[-1], "") == ch:
                tracker.pop()
            else:
                tracker.append(ch)
        return not tracker
        