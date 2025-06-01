class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import defaultdict

        seq_len = len(s)

        word_len = len(words[0])
        n_words = len(words)
        word_hash = defaultdict(int)
        for word in words:
            word_hash[word] += 1
        
        build_hash = defaultdict(int)
        result = []

        for offset in range(word_len):
            left = offset
            build_hash.clear()
            count = 0

            for right in range(left, seq_len - word_len + 1, word_len):

                chunk = s[right: right + word_len]
                if chunk in word_hash:
                    build_hash[chunk] += 1
                    count += 1

                    while build_hash[chunk] > word_hash[chunk]:
                        left_word = s[left: left + word_len]
                        build_hash[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == n_words:
                        result.append(left)
                else: 
                    build_hash.clear()
                    count = 0 
                    left = right + word_len
        return result