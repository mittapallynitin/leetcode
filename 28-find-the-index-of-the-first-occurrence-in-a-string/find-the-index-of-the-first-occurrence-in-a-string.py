class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        strings = haystack.split(needle)
        if len(strings) > 1:
            return len(strings[0])
        return -1