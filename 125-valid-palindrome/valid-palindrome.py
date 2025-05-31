class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ch for ch in s.lower() if ch.isalnum()]
        return s == s[::-1]

        