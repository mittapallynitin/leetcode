class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        for ch1, ch2 in zip(first, last):
            if ch1 == ch2:
                ans += ch1
            else:
                break
        return ans
