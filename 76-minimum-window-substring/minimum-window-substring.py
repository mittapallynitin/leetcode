class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict

        # S Details
        seq_len = len(s)
        
        # T Details
        char_hash = defaultdict(int)
        required_len = len(t)
        for ch in t:
            char_hash[ch] += 1

        # Build details
        build_hash = defaultdict(int)
        build_len = 0

        # Result
        window = float("inf")
        answer = ""
        l = 0 

        # Validate window
        def is_valid(build_hash):
            for ch in char_hash:
                if build_hash.get(ch, 0) < char_hash[ch]:
                    return False
            return True


        for r in range(seq_len):
            if s[r] in char_hash:
                build_hash[s[r]] += 1
                build_len += 1

            while build_len >= required_len and is_valid(build_hash):
                window_len = r - l + 1
                if window_len < window:
                    window = window_len
                    answer = s[l:r + 1]

                left_ch = s[l]
                if left_ch in build_hash:
                    build_hash[left_ch] -= 1
                    build_len -= 1
                l += 1
        
        return answer


