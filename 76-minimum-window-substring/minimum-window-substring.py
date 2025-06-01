class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict, Counter

        if not s or not t:
            return ""

        # S Details
        seq_len = len(s)
        
        # T Details
        char_hash = Counter(t)
        required = len(char_hash)
        

        # Build details
        formed = 0
        build_hash = defaultdict(int)

        # Result
        window = float("inf")
        answer = ""
        l = 0 


        for r in range(seq_len):
            ch = s[r]
            if ch in char_hash:
                build_hash[ch] += 1
                if char_hash[ch] == build_hash[ch]:
                    formed += 1

            while formed == required:
                window_len = r - l + 1
                if window_len < window:
                    window = window_len
                    answer = s[l:r + 1]

                left_ch = s[l]
                if left_ch in build_hash:
                    build_hash[left_ch] -= 1
                    if build_hash[left_ch] < char_hash[left_ch]:
                        formed -= 1
                    
                l += 1
        
        return answer


