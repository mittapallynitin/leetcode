class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pw_map = dict()
        wp_map = dict()

        words = s.split()

        if len(pattern) != len(words): return False

        for pt, word in zip(pattern, words):

            if (
                (pt in pw_map and pw_map[pt] != word) or 
                (word in wp_map and wp_map[word] != pt)
            ):
                return False

            pw_map[pt] = word
            wp_map[word] = pt
        return True