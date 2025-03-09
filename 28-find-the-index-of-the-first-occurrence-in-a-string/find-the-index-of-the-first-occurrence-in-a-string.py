class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_size = len(haystack)
        needle_size = len(needle)

        for ans in range(haystack_size):
            hay_p = ans
            ned_p = 0
            while hay_p < haystack_size and haystack[hay_p] == needle[ned_p]:
                hay_p += 1
                ned_p += 1
                if ned_p == len(needle):
                    return ans
        return -1


