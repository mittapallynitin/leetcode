class Solution:
    def isValid(self, s: str) -> bool:
        complement = {
            "(" : ")", 
            "{" : "}",
            "[" : "]"
        }

        tracker = []

        for ch in s:
            if tracker and ch == complement.get(tracker[-1]):
                tracker.pop()
            else:
                tracker.append(ch)
        return not tracker
        