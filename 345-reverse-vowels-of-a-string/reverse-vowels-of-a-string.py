class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        v = []
        for ch in s:
            if ch in vowels:
                v.append(ch)
        res = []
        for ch in s:
            if ch in vowels:
                res.append(v.pop())
            else:
                res.append(ch)
        return "".join(res)
        