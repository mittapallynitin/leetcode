class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter, defaultdict
        word_len = len(words[0])
        seq_len = len(s)
        n_words = len(words)
        total_len = word_len * n_words
        word_hash = defaultdict(int)
        build_hash = defaultdict(int)
        for word in words: word_hash[word] += 1
        result = []

        for i in range(word_len):
            left = i
            build_hash.clear()
            count = 0
            for j in range(i, seq_len - word_len+1, word_len):
                chunk = s[j: j+word_len]
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
                    left = j + word_len
        return result
                

