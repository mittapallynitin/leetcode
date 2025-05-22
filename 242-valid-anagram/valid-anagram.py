class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alpha = [0]*26
        for ch1, ch2 in zip(s, t):
            ch1 = ord(ch1) - ord('a')
            ch2 = ord(ch2) - ord('a')
            alpha[ch1] += 1
            alpha[ch2] -= 1

        for i in range(26):
            if alpha[i] != 0:
                return False
        return True


        