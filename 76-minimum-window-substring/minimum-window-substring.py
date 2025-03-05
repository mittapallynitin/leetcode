class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def isValid(tracker, vals):
            for key in vals:
                if key not in tracker or tracker[key] < vals[key]:
                    return False
            return True
    
        required = {}
        for ch in t:
            required[ch] = required.get(ch, 0) + 1
        l = 0 
        min_window = float("inf")
        tracker = {}
        answer = ""
        for r in range(len(s)):
            if s[r] in required:
                tracker[s[r]] = tracker.get(s[r], 0) + 1
            while isValid(tracker, required):
                if r - l + 1 < min_window:
                    min_window = r - l +1
                    answer = s[l:r+1]
                if s[l] in required:
                    tracker[s[l]] -= 1
                l += 1
        return answer