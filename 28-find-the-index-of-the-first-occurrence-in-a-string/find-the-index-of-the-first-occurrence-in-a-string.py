class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_size = len(haystack)
        needle_size = len(needle)

        if haystack_size < needle_size:
            return -1

        for ans in range(haystack_size):
            if haystack[ans: ans+needle_size] == needle:
                return ans

        return -1


