class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_map = {}
        t_map = {}
        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1
        
        for ch in t:
            if ch in s_map and t_map[ch] == s_map[ch]:
                continue
            return ch

        