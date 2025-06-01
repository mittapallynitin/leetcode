class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l, r = 0, len(s)
        window = 0
        for i in range(r):
            while s[i] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[i])
            window = max(window, len(visited))
        return window
                

        