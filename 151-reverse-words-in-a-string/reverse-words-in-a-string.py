class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return " ".join([w for w in s[::-1] if w.strip()])