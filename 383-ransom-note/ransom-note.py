class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ch_count = {}
        for ch in magazine:
            ch_count[ch] = ch_count.get(ch, 0) + 1
        
        for ch in ransomNote:
            if ch in ch_count:
                ch_count[ch] -= 1
                if ch_count[ch] < 0:
                    return False
            else:
                return False
        return True
        