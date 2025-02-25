class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l = 0
        count = 0
        counter = {'0': 0, '1': 0}

        for r in range(len(s)):
            counter[s[r]] += 1
            while counter['0'] > k and counter['1'] > k:
                counter[s[l]] -= 1
                l += 1
            count += r - l + 1
        return count


