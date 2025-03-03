class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = set('aeiou') 
        res = 0
        for ch in s[:k]:
            if ch in vowels:
                count += 1
        res = max(res, count)

        for r in range(k, len(s)):
            if s[r-k] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1
            res = max(res, count)
        return res
        