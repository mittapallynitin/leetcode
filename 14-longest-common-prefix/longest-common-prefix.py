class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for chrs in zip(*map(list,strs)):
            ch = chrs[0]
            if all(map(lambda x: x == ch, chrs)):
                ans += ch
            else:
                break
        return ans