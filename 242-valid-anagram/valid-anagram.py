class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alpha = dict()
        for ch1, ch2 in zip(s, t):
            alpha[ch1] = alpha.get(ch1, 0) +  1
            alpha[ch2] = alpha.get(ch2, 0) - 1

        for i in alpha:
            if alpha[i] != 0:
                return False
        return True


        