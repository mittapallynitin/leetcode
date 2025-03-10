class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_cnt, t_cnt = dict(), dict()
        for c1, c2 in zip(s, t): 
            s_cnt[c1] = s_cnt.get(c1, 0) + 1
            t_cnt[c2] = t_cnt.get(c2, 0) + 1
        return s_cnt == t_cnt
        